#Scrie o functie care imparte doua numere. Functia ar trebui sa gestioneze exceptia de impartire la zero.
def imparte_numere():
    try:
        a = float(input("Introduceți numărătorul: "))
        b = float(input("Introduceți numitorul: "))
        rezultat = a / b
        print(f"Rezultatul împărțirii este: {rezultat}")
    except ZeroDivisionError:
        print("Eroare: Împărțirea la zero nu este permisă.")
    except ValueError:
        print("Eroare: Vă rugăm să introduceți doar numere valide.")
imparte_numere()
