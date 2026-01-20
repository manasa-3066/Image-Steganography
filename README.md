# Secure Image Steganography System

This project implements **Image Steganography and Reverse Steganography**
using the **Least Significant Bit (LSB)** technique.

The system allows a user to hide a **single character** inside a **grayscale JPEG image**
and later retrieve it securely.

---

## 📌 Features

- Grayscale JPEG image processing  
- Standard size conversion (**128 × 128**)  
- LSB-based character hiding  
- Stego image generation  
- Reverse steganography (character extraction)  
- Text-to-Speech for extracted character  
- Two user interfaces:
  - **Desktop Application:** Tkinter  
  - **Web Application:** Streamlit  

---

## 🧠 Steganography Workflow

1. User selects a JPEG image  
2. Image is converted to grayscale  
3. Image is resized to a standard size (128 × 128)  
4. Character is hidden using LSB steganography  
5. Stego image is generated  
6. Reverse steganography extracts the character  
7. Extracted character is converted to speech  

---

## 🖥️ Desktop Application (Tkinter)

The Tkinter-based application provides a **wizard-style desktop interface**
that guides the user step-by-step through the steganography process.

### Flow
- Select Image  
- Preprocess Image  
- Hide Character  
- Retrieve Character & Speech  

### ▶️ Run Tkinter App

```bash
py -3.10 tkinter_app/tkinter_app.py

### 🌐 Web Application (Streamlit)

The Streamlit-based application provides a web-based user interface
with a visual pipeline for each stage of steganography.

Features

Upload JPEG image

Image preprocessing (grayscale + 128 × 128)

Stego image generation

Reverse steganography

Automatic speech output in browser

▶️ Run Streamlit App
py -3.10 -m streamlit run streamlit_app/app.py

📦 Requirements

Install all dependencies using:

pip install -r requirements.txt

🧑‍🏫 Academic Note

This project was developed as part of an academic assignment
to demonstrate the concept of secure data hiding using image steganography.
