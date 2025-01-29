import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
from collections import Counter

SITE_URL = "https://www.bbc.com/news"
def colecteaza_date(url):
    try:
        raspuns = requests.get(url)
        if raspuns.status_code != 200:
            print(f"Eroare la accesarea site-ului: {raspuns.status_code}")
            return []

        soup = BeautifulSoup(raspuns.text, 'html.parser')

        articole = []
        for articol in soup.find_all('div', class_='gs-c-promo'):  # Clasă specifică pentru articole
            titlu = articol.find('h3')
            rezumat = articol.find('p')
            link = articol.find('a', href=True)

            if titlu and rezumat and link:
                articole.append({
                    "titlu": titlu.text.strip(),
                    "rezumat": rezumat.text.strip(),
                    "url": "https://www.bbc.com" + link['href']
                })
        return articole
    except Exception as e:
        print(f"A apărut o eroare: {e}")
        return []


def salveaza_csv(nume_fisier, articole):
    try:
        with open(nume_fisier, mode='w', encoding='utf-8', newline='') as fisier_csv:
            writer = csv.DictWriter(fisier_csv, fieldnames=["titlu", "rezumat", "url"])
            writer.writeheader()
            writer.writerows(articole)
        print(f"Datele au fost salvate în fișierul {nume_fisier}")
    except Exception as e:
        print(f"Eroare la salvarea fișierului CSV: {e}")


def filtreaza_articole(articole, cuvant_cheie):
    return [articol for articol in articole if cuvant_cheie.lower() in articol['titlu'].lower()]

def vizualizeaza_categorii(articole):
    categorii = [articol['titlu'].split(':')[0] for articol in articole if ':' in articol['titlu']]
    frecventa_categorii = Counter(categorii)

    plt.bar(frecventa_categorii.keys(), frecventa_categorii.values(), color='skyblue')
    plt.title('Distribuția articolelor pe categorii')
    plt.xlabel('Categorie')
    plt.ylabel('Număr articole')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    print("Se colectează datele de pe site...")
    articole = colecteaza_date(SITE_URL)

    if not articole:
        print("Nu s-au găsit articole.")
        return

    nume_fisier = "articole_stiri.csv"
    salveaza_csv(nume_fisier, articole)
    cuvant_cheie = input("Introduceți un cuvânt cheie pentru filtrarea articolelor: ")
    articole_filtrate = filtreaza_articole(articole, cuvant_cheie)

    if articole_filtrate:
        print(f"Articole care conțin cuvântul cheie '{cuvant_cheie}':")
        for articol in articole_filtrate:
            print(f"- {articol['titlu']} - {articol['rezumat']}")
    else:
        print(f"Niciun articol nu conține cuvântul cheie '{cuvant_cheie}'.")
    vizualizeaza_categorii(articole)


if __name__ == "__main__":
    main()
