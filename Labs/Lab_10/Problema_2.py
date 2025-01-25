#Creeaza o functie care citeste un fisier text ce contine numere pe fiecare linie.
#Functia ar trebui sa calculeze suma acestor numere, gestionand exceptiile pentru fisier
#inexistent, erori de citire si valori nevalide.

def suma_numerelor_din_fisier(nume_fisier):
    try:
        with open(nume_fisier, 'r') as fisier:
            suma = 0
            for linie in fisier:
                try:
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Eroare: Linia '{linie.strip()}' nu este un număr valid. Aceasta va fi ignorată.")
            return suma
    except FileNotFoundError:
        return f"Eroare: Fișierul '{nume_fisier}' nu există."
    except IOError:
        return "Eroare: A apărut o problemă la citirea fișierului."

nume_fisier = "numere.txt"  # Numele fișierului
rezultat = suma_numerelor_din_fisier(nume_fisier)
print(f"Rezultatul: {rezultat}")
