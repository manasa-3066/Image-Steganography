import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pyttsx3

# -------- GLOBAL DATA (CONNECTIVITY) --------
original_image = None
processed_image = None
stego_image = None

# -------- IMAGE LOGIC --------
def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))
    return img

def hide_character(image, char):
    binary = format(ord(char), "08b")
    flat = image.flatten()

    for i in range(8):
        flat[i] = (flat[i] & 254) | int(binary[i])

    stego = flat.reshape(image.shape)
    cv2.imwrite("stego_image.png", stego)
    return stego

def extract_character():
    img = cv2.imread("stego_image.png", cv2.IMREAD_GRAYSCALE)
    flat = img.flatten()
    bits = ""

    for i in range(8):
        bits += str(flat[i] & 1)

    return chr(int(bits, 2))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# -------- STEP 1: SELECT IMAGE --------
def step1():
    global original_image

    path = filedialog.askopenfilename(
        filetypes=[("JPEG Images", "*.jpg *.jpeg")]
    )

    if not path:
        return

    original_image = path
    step1_window.destroy()
    step2()

# -------- STEP 2: SHOW PREPROCESSED IMAGE --------
def step2():
    global processed_image

    processed_image = preprocess_image(original_image)

    win = tk.Tk()
    win.title("Step 2: Preprocessed Image")
    win.geometry("500x500")

    tk.Label(win, text="Step 2: Grayscale & Standard Size (128×128)",
             font=("Arial", 14)).pack(pady=10)

    img = Image.fromarray(processed_image)
    img_tk = ImageTk.PhotoImage(img.resize((250, 250)))

    label = tk.Label(win, image=img_tk)
    label.image = img_tk
    label.pack(pady=10)

    tk.Button(win, text="Next → Hide Character",
              bg="green", fg="white",
              command=lambda: [win.destroy(), step3()]
              ).pack(pady=10)

    win.mainloop()

# -------- STEP 3: HIDE CHARACTER --------
def step3():
    def hide():
        global stego_image
        char = entry.get()

        if len(char) != 1:
            messagebox.showerror("Error", "Enter exactly ONE character")
            return

        stego_image = hide_character(processed_image, char)

        img = Image.fromarray(stego_image)
        img_tk = ImageTk.PhotoImage(img.resize((250, 250)))

        label.config(image=img_tk)
        label.image = img_tk

        messagebox.showinfo("Success", "Character hidden successfully")

    win = tk.Tk()
    win.title("Step 3: Hide Character")
    win.geometry("500x520")

    tk.Label(win, text="Step 3: Hide Character using LSB",
             font=("Arial", 14)).pack(pady=10)

    tk.Label(win, text="Enter Secret Character").pack()
    entry = tk.Entry(win)
    entry.pack(pady=5)

    tk.Button(win, text="Hide Character", bg="#d97706",
              fg="white", command=hide).pack(pady=5)

    label = tk.Label(win)
    label.pack(pady=10)

    tk.Button(win, text="Next → Retrieve Character",
              bg="green", fg="white",
              command=lambda: [win.destroy(), step4()]
              ).pack(pady=10)

    win.mainloop()

# -------- STEP 4: RETRIEVE & SPEAK --------
def step4():
    def retrieve():
        ch = extract_character()
        result.config(text=f"Retrieved Character: {ch}")
        speak(ch)

    def exit_app():
        win.destroy()

    win = tk.Tk()
    win.title("Step 4: Reverse Steganography")
    win.geometry("500x350")

    tk.Label(win, text="Step 4: Reverse Steganography",
             font=("Arial", 14)).pack(pady=10)

    tk.Button(win, text="Retrieve Character",
              bg="#2563eb", fg="white",
              command=retrieve).pack(pady=10)

    result = tk.Label(win, text="", font=("Arial", 16))
    result.pack(pady=20)

    tk.Button(win, text="Exit Application",
              bg="red", fg="white",
              command=exit_app).pack(pady=10)

    win.mainloop()

# -------- START APPLICATION --------
step1_window = tk.Tk()
step1_window.title("Secure Image Steganography System")
step1_window.geometry("400x250")

tk.Label(step1_window, text="Secure Image Steganography System",
         font=("Arial", 16)).pack(pady=20)

tk.Button(step1_window, text="Select JPEG Image",
          bg="#2563eb", fg="white",
          command=step1).pack(pady=20)

step1_window.mainloop()
