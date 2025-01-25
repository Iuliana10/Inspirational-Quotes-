#Creeaza un program care simuleaza un sistem de gestionare a unui inventar
#de produse. Utilizatorul va putea adauga produse, cauta produse dupa nume si va putea
#actualiza cantitatea unui produs. Programul va gestiona exceptiile pentru intrari nevalide si
#produse inexistente.

class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        try:
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] += cantitate
            else:
                self.produse[nume] = cantitate
            print(f"Produsul '{nume}' a fost adăugat/actualizat cu succes.")
        except ValueError as e:
            print(f"Eroare: {e}")

    def cauta_produs(self, nume):
        try:
            if nume in self.produse:
                print(f"Produs: {nume}, Cantitate: {self.produse[nume]}")
            else:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
        except KeyError as e:
            print(e)

    def actualizeaza_cantitatea(self, nume, cantitate):
        try:
            if cantitate < 0:
                raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
            if nume in self.produse:
                self.produse[nume] = cantitate
                print(f"Produsul '{nume}' a fost actualizat cu succes.")
            else:
                raise KeyError(f"Produsul '{nume}' nu există în inventar.")
        except (ValueError, KeyError) as e:
            print(f"Eroare: {e}")

    def afiseaza_inventar(self):
        if not self.produse:
            print("Inventarul este gol.")
        else:
            print("Inventar curent:")
            for nume, cantitate in self.produse.items():
                print(f"- {nume}: {cantitate}")


def meniu():
    inventar = Inventar()
    while True:
        print("\nMeniu:")
        print("1. Adaugă produs")
        print("2. Caută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Afișează inventarul")
        print("5. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            nume = input("Introduceți numele produsului: ")
            try:
                cantitate = int(input("Introduceți cantitatea: "))
                inventar.adauga_produs(nume, cantitate)
            except ValueError:
                print("Eroare: Cantitatea trebuie să fie un număr întreg.")
        elif optiune == "2":
            nume = input("Introduceți numele produsului de căutat: ")
            inventar.cauta_produs(nume)
        elif optiune == "3":
            nume = input("Introduceți numele produsului: ")
            try:
                cantitate = int(input("Introduceți noua cantitate: "))
                inventar.actualizeaza_cantitatea(nume, cantitate)
            except ValueError:
                print("Eroare: Cantitatea trebuie să fie un număr întreg.")
        elif optiune == "4":
            inventar.afiseaza_inventar()
        elif optiune == "5":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să încercați din nou.")

meniu()
