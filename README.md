# 📱 Générateur de Codes QR
Application graphique Tkinter – QR Code personnalisé (couleurs, tailles, export PNG/JPG)
![Aperçu de l'application](illustration1.png)

## 🚀 Description

Cette application est un générateur de QR Codes personnalisés développé en Python avec Tkinter.
Elle permet à l’utilisateur de :

- Générer un QR Code à partir d’un texte ou d’une URL

- Personnaliser :

  - la taille du QR code (100px → 1000px)

  - la couleur du QR

  - la couleur de fond

- Afficher un aperçu du QR Code généré

- Sauvegarder le QR Code au format <b>PNG</b> ou <b>JPG</b>

L’interface est pensée pour être simple, intuitive et compatible Windows / Mac / Linux.

## 🎨 Fonctionnalités
### 🖊️ 1. Entrée du texte

C'est une zone de texte permettant de saisir :

- URL

- phrase

- texte long

- identifiant

- clé Wi-Fi, etc.

### 🎛 2. Options de personnalisation

L’utilisateur peut choisir :

- ✔ Taille de l’image

- ➡ de 100 px à 1000 px

- ✔ Couleur du QR : black, red, blue, #ff0000, etc.

- ✔ Couleur de fond : white, #fafafa, etc.

### 🖼️ 3. Prévisualisation en direct

Le QR code généré apparaît directement dans une zone dédiée.

### 💾 4. Exportation du QR Code

- PNG (par défaut)

- JPG

Nom du fichier choisi par l’utilisateur

## 📦 Installation
### 1. Installer Python (3.8+ recommandé)

https://www.python.org/downloads/

### 2. Installer les dépendances

```bash
pip install qrcode[pil] pillow
```

## 🛠 Technologies utilisées
| Technologie      | Utilité                           |
| ---------------- | --------------------------------- |
| **Tkinter**      | Interface graphique               |
| **qrcode**       | Génération QR                     |
| **Pillow (PIL)** | Manipulation d’images + affichage |
| **io**           | Conversion mémoire tampon         |


## ⚠️ Limitations actuelles

- Pas de prévisualisation du QR avant validation

- Pas de choix via sélecteur de couleurs (entrée manuelle)

- Pas d’export SVG

- Une seule génération à la fois

## 💡 Améliorations possibles

- ✔ Ajouter un sélecteur de couleurs (tkinter.colorchooser)

- ✔ Générer des QR Codes en SVG

- ✔ Ajouter un logo au centre du QR

- ✔ Générer plusieurs QR depuis un fichier Excel (batch)

- ✔ Ajouter un thème moderne (ttkbootstrap)

- ✔ Ajouter un bouton "Copier dans le presse-papier"

## 📜 Auteur

Cyr DJOKI

![Aperçu de l'application](illustration2.png)
