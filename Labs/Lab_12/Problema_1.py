"""Scrieti un script Python care interactioneaza cu API-ul
https://jsonplaceholder.typicode.com/users, care furnizeaza informatii fictive despre utilizatori.
Scriptul trebuie sa indeplineasca urmatoarele cerinte:"""

import requests
from tabulate import tabulate

def obtine_utilizatori():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        raspuns = requests.get(url)
        raspuns.raise_for_status()
        return raspuns.json()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea datelor: {e}")
        return None


def afiseaza_utilizatori(utilizatori):
    date_tabel = []
    for utilizator in utilizatori:
        date_tabel.append([
            utilizator["id"], utilizator["name"], utilizator["username"], utilizator["email"],
            utilizator["address"]["city"], utilizator["company"]["name"],
            utilizator["phone"], utilizator["website"]
        ])
    antete = ["ID", "Nume", "Username", "Email", "Oraș", "Companie", "Telefon", "Website"]
    print(tabulate(date_tabel, headers=antete, tablefmt="grid"))


def filtreaza_utilizatori_dupa_oras(utilizatori, oras):
    return [utilizator for utilizator in utilizatori if utilizator["address"]["city"].lower() == oras.lower()]


def main():
    utilizatori = obtine_utilizatori()
    if utilizatori:
        oras = input("Introduceți orașul pentru filtrare (lăsați gol pentru toți utilizatorii): ").strip()
        if oras:
            utilizatori = filtreaza_utilizatori_dupa_oras(utilizatori, oras)

        if utilizatori:
            afiseaza_utilizatori(utilizatori)
        else:
            print("Nu au fost găsiți utilizatori în acest oraș.")


if __name__ == "__main__":
    main()
