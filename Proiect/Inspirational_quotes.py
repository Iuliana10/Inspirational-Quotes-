#Site https://citate.top/categorii/inspirationale/
#am instalat in terminal pip install requests beautifulsoup4
import requests  #o bibliotecă care permite trimiterea de cereri HTTP pentru a obține conținutul paginilor web.
from bs4 import BeautifulSoup #o bibliotecă care analizează paginile HTML pentru a extrage date
import tkinter as tk
from tkinter import messagebox #permite afisarea unui mesaj de eroare
import random #pentru alegerea aleatoare a unui citat

def get_citate():
    url = "https://citate.top/categorii/inspirationale/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    #user-agent previne blocarea cererilor
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        citate_elements = soup.find_all("div", class_="song-item-text single-citat-text") # cauta toate elementele html care contin citate
        citate = [elem.find("p").get_text(strip=True) for elem in citate_elements if elem.find("p")]
        return citate
    else:
        messagebox.showerror("Eroare", f"Nu am putut accesa site-ul. Cod de eroare: {response.status_code}")
        return []

def show_random_citat():
    if citate:
        citat = random.choice(citate)
        citate.remove(citat)
        used_citate.append(citat)
        citat_label.config(text=citat, fg="blue", bg="lightyellow", wraplength=500)
        used_label.config(text="Citate folosite:\n" + "\n".join(used_citate), fg="purple")

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
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

citat_label = tk.Label(frame, text="Apasă pe buton pentru un citat!", font=("Arial", 14), wraplength=500, justify="center", fg="blue")
citat_label.pack(pady=20)

random_button = tk.Button(frame, text="Afișează un citat", command=show_random_citat, font=("Arial", 12), fg="red")
random_button.pack(pady=5)

refresh_button = tk.Button(frame, text="Reîncarcă citatele", command=refresh_citate, font=("Arial", 12), fg="red")
refresh_button.pack(pady=5)

used_label = tk.Label(root, text="", font=("Arial", 10), justify="left", fg="purple")
used_label.pack(pady=10)

citate = get_citate()
used_citate = []
root.mainloop()