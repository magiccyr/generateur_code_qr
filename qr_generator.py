import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import io


class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Codes QR")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Variable pour stocker l'image QR
        self.qr_image = None
        
        # Configuration de l'interface
        self.setup_ui()
    
    def setup_ui(self):
        # Canvas et scrollbar pour le défilement
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        
        # Frame principal avec scrolling
        main_frame = ttk.Frame(canvas, padding="20")
        
        # Configurer le canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Créer une fenêtre dans le canvas
        canvas_frame = canvas.create_window((0, 0), window=main_frame, anchor=tk.NW)
        
        # Mettre à jour la zone de défilement
        def configure_scroll(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_frame, width=event.width)
        
        main_frame.bind("<Configure>", configure_scroll)
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_frame, width=e.width))
        
        # Permettre le défilement avec la molette de la souris
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        # Titre
        title_label = ttk.Label(
            main_frame, 
            text="Générateur de Codes QR", 
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Frame pour la saisie
        input_frame = ttk.LabelFrame(main_frame, text="Données", padding="10")
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(input_frame, text="Entrez le texte ou l'URL :").pack(anchor=tk.W)
        self.text_entry = tk.Text(input_frame, height=4, width=50, wrap=tk.WORD)
        self.text_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Frame pour les options
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Taille
        size_frame = ttk.Frame(options_frame)
        size_frame.pack(fill=tk.X, pady=5)
        ttk.Label(size_frame, text="Taille (pixels) :").pack(side=tk.LEFT)
        self.size_var = tk.StringVar(value="300")
        size_spinbox = ttk.Spinbox(
            size_frame, 
            from_=100, 
            to=1000, 
            textvariable=self.size_var,
            width=10
        )
        size_spinbox.pack(side=tk.LEFT, padx=(10, 0))
        
        # Couleur de remplissage
        color_frame = ttk.Frame(options_frame)
        color_frame.pack(fill=tk.X, pady=5)
        ttk.Label(color_frame, text="Couleur :").pack(side=tk.LEFT)
        self.fill_color_var = tk.StringVar(value="black")
        fill_color_entry = ttk.Entry(color_frame, textvariable=self.fill_color_var, width=15)
        fill_color_entry.pack(side=tk.LEFT, padx=(10, 0))
        
        # Couleur de fond
        bg_color_frame = ttk.Frame(options_frame)
        bg_color_frame.pack(fill=tk.X, pady=5)
        ttk.Label(bg_color_frame, text="Fond :").pack(side=tk.LEFT)
        self.bg_color_var = tk.StringVar(value="white")
        bg_color_entry = ttk.Entry(bg_color_frame, textvariable=self.bg_color_var, width=15)
        bg_color_entry.pack(side=tk.LEFT, padx=(10, 0))
        
        # Bouton de génération
        generate_btn = ttk.Button(
            main_frame, 
            text="Générer le Code QR", 
            command=self.generate_qr
        )
        generate_btn.pack(pady=10)
        
        # Frame pour afficher le QR code
        self.display_frame = ttk.LabelFrame(main_frame, text="Code QR Généré", padding="10")
        self.display_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.qr_label = ttk.Label(self.display_frame, text="Le code QR apparaîtra ici")
        self.qr_label.pack(expand=True)
        
        # Bouton de sauvegarde
        self.save_btn = ttk.Button(
            main_frame, 
            text="Sauvegarder l'image", 
            command=self.save_qr,
            state=tk.DISABLED
        )
        self.save_btn.pack()
    
    def generate_qr(self):
        # Récupérer le texte
        text = self.text_entry.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Attention", "Veuillez entrer du texte ou une URL !")
            return
        
        try:
            # Créer le code QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            # Générer l'image
            fill_color = self.fill_color_var.get()
            bg_color = self.bg_color_var.get()
            img = qr.make_image(fill_color=fill_color, back_color=bg_color)
            
            # Redimensionner
            size = int(self.size_var.get())
            img = img.resize((size, size), Image.Resampling.LANCZOS)
            
            # Stocker l'image
            self.qr_image = img
            
            # Convertir pour affichage dans tkinter
            img_tk = ImageTk.PhotoImage(img)
            self.qr_label.configure(image=img_tk, text="")
            self.qr_label.image = img_tk  # Garder une référence
            
            # Activer le bouton de sauvegarde
            self.save_btn.configure(state=tk.NORMAL)
            
            messagebox.showinfo("Succès", "Code QR généré avec succès !")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération : {str(e)}")
    
    def save_qr(self):
        if self.qr_image is None:
            return
        
        # Demander où sauvegarder
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.qr_image.save(file_path)
                messagebox.showinfo("Succès", f"Image sauvegardée : {file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde : {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()