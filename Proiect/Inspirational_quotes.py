#Site https://citate.top/celebre/agatha-christie/
#am instalat in terminal pip install requests beautifulsoup4
import requests  #o bibliotecă care permite trimiterea de cereri HTTP pentru a obține conținutul paginilor web.
from bs4 import BeautifulSoup #o bibliotecă care analizează paginile HTML pentru a extrage date
import tkinter as tk #crearea de interfețe grafice (ferestre).
from tkinter import messagebox #o componentă din tkinter pentru a afișa ferestre de dialog cu mesaje.
import random #pentru alegerea aleatoare a unui citat


# Funcție pentru a prelua citate
def get_citate():
    url = "https://citate.top/celebre/agatha-christie/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Căutăm div-urile care conțin citatele
        citate_elements = soup.find_all("div", class_="song-item-text single-citat-text")

        # Extragem textul din fiecare element
        citate = []
        for elem in citate_elements:
            p_tag = elem.find("p")  # căutăm elementul <p>
            if p_tag:
                citate.append(p_tag.get_text(strip=True))  # extragem textul fără spații suplimentare
        return citate
    else:
        messagebox.showerror("Eroare", f"Nu am putut accesa site-ul. Cod de eroare: {response.status_code}")
        return []


# Funcție pentru afișarea unui citat aleatoriu
def show_random_citat():
    if citate:
        citat = random.choice(citate)
        citat_label.config(text=citat, wraplength=500)
    else:
        citat_label.config(text="Nu sunt citate disponibile.")


# Preluăm citatele
def refresh_citate():
    global citate
    citate = get_citate()
    if citate:
        show_random_citat()


# Interfața grafică
root = tk.Tk()
root.title("Citate Agatha Christie")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

citat_label = tk.Label(frame, text="Apasă pe buton pentru un citat!", font=("Arial", 14), wraplength=500,
                       justify="center")
citat_label.pack(pady=20)

random_button = tk.Button(frame, text="Afișează un citat", command=show_random_citat, font=("Arial", 12))
random_button.pack(pady=5)

refresh_button = tk.Button(frame, text="Reîncarcă citatele", command=refresh_citate, font=("Arial", 12))
refresh_button.pack(pady=5)

# Preluăm citate la început
citate = get_citate()

root.mainloop()
