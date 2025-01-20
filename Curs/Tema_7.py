class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False

    def __str__(self):
        status = "împrumutată" if self.este_imprumutata else "disponibilă"
        return f"{self.titlu} de {self.autor} (ISBN: {self.isbn}) - {status}"


class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            self.carti_imprumutate.append(carte)
            carte.este_imprumutata = True
            print(f"{self.nume} a împrumutat cartea: {carte.titlu}")
        else:
            print(f'Cartea "{carte.titlu}" este deja împrumutată.')
    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
                    self.carti_imprumutate.remove(carte)
                    carte.este_imprumutata = False
                    print(f"{self.nume} a returnat cartea: {carte.titlu}")
        else:
                    print(f"{self.nume} nu are cartea {carte.titlu} înregistrată ca împrumutată.")

class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea {carte.titlu} a fost adăugată în bibliotecă.")

    def sterge_carte(self, carte):
        if carte in self.carti:
            self.carti.remove(carte)
            print(f"Cartea {carte.titlu} a fost ștearsă din bibliotecă.")
        else:
            print(f"Cartea {carte.titlu} nu se află în bibliotecă.")

    def listeaza_carti_disponibile(self):
        print("Cărțile disponibile în bibliotecă:")
        for carte in self.carti:
            if not carte.este_imprumutata:
                print(carte)


def creeaza_carti_si_membri():
    biblioteca = Biblioteca()

    numar_carti = int(input("Introduceți numărul de cărți de adăugat: "))
    for _ in range(numar_carti):
        titlu = input("Introduceți titlul cărții: ")
        autor = input("Introduceți autorul cărții: ")
        isbn = input("Introduceți ISBN-ul cărții: ")
        carte = Carte(titlu, autor, isbn)
        biblioteca.adauga_carte(carte)

    numar_membri = int(input("Introduceți numărul de membri ai bibliotecii: "))
    membri = []
    for _ in range(numar_membri):
        nume = input("Introduceți numele membrului: ")
        membru = MembruBiblioteca(nume)
        membri.append(membru)

    return biblioteca, membri

if __name__ == "__main__":
    biblioteca, membri = creeaza_carti_si_membri()

    while True:
        print("\nMeniu:")
        print("1. Împrumută o carte")
        print("2. Returnează o carte")
        print("3. Listează cărțile disponibile")
        print("4. Ieșire")
        optiune = input("Alegeți o opțiune: ")

        if optiune == "1":
            nume_membru = input("Introduceți numele membrului: ")
            titlu_carte = input("Introduceți titlul cărții: ")
            membru = next((m for m in membri if m.nume == nume_membru), None)
            carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)
            if membru and carte:
                membru.imprumuta_carte(carte)
            else:
                print("Membru sau carte invalidă.")

        elif optiune == "2":
            nume_membru = input("Introduceți numele membrului: ")
            titlu_carte = input("Introduceți titlul cărții: ")
            membru = next((m for m in membri if m.nume == nume_membru), None)
            carte = next((c for c in biblioteca.carti if c.titlu == titlu_carte), None)
            if membru and carte:
                membru.returneaza_carte(carte)
            else:
                print("Membru sau carte invalidă.")

        elif optiune == "3":
            biblioteca.listeaza_carti_disponibile()

        elif optiune == "4":
            break

        else:
            print("Opțiune invalidă. Vă rugăm să alegeți din nou.")
