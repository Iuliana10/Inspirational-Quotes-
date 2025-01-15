# Site-ul: https://citate.top/categorii/inspirationale/
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Funcția pentru a obține citate
def get_citate():
    url = "https://citate.top/categorii/inspirationale/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        citate_elements = soup.find_all("div", class_="song-item-text single-citat-text")
        citate = [elem.find("p").get_text(strip=True) for elem in citate_elements if elem.find("p")]
        return citate
    else:
        messagebox.showerror("Eroare", f"Nu am putut accesa site-ul. Cod de eroare: {response.status_code}")
        return []

# Funcția pentru a afișa un citat aleatoriu
def show_random_citat():
    if citate:
        citat = random.choice(citate)
        citate.remove(citat)
        used_citate.append(citat)
        citat_label.config(text=citat, fg="blue", bg="lightyellow", wraplength=500)
        used_label.config(text="Citate folosite:\n" + "\n".join(wrap_text(c) for c in used_citate), fg="purple")

# Funcția pentru a împărți textul lung pe linii
def wrap_text(text, line_length=80):
    words = text.split()
    lines, current_line = [], []
    current_length = 0
    for word in words:
        if current_length + len(word) + len(current_line) > line_length:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)
    if current_line:
        lines.append(" ".join(current_line))
    return "\n".join(lines)

# Funcția pentru a reîncărca citatele
def refresh_citate():
    global citate, used_citate
    citate = get_citate()
    used_citate.clear()
    used_label.config(text="")
    if citate:
        show_random_citat()

# Interfața grafică
root = tk.Tk()
root.title("Citate Inspirationale")
root.geometry("800x500")

# Încarcă și redimensionează imaginea de fundal
background_image_path = "fundal proiect 1.jpeg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((800, 500), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)

# Crearea unui label pentru fundal
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

citat_label = tk.Label(frame, text="Apasă pe buton pentru un citat!", font=("Arial", 14), wraplength=500, justify="center", fg="blue", bg="lightyellow")
citat_label.pack(pady=20)

button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=5)

random_button = tk.Button(button_frame, text="Afișează un citat", command=show_random_citat, font=("Arial", 12), fg="green")
random_button.pack(side="left", padx=10)

refresh_button = tk.Button(button_frame, text="Reîncarcă citatele", command=refresh_citate, font=("Arial", 12), fg="red")
refresh_button.pack(side="right", padx=10)

used_label = tk.Label(root, text="", font=("Arial", 14), justify="left", fg="purple", bg="white")
used_label.pack(pady=10)

citate = get_citate()
used_citate = []
root.mainloop()
