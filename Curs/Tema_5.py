#Sistem de Evaluare a Filmelor care citește datele despre filme dintr-un fișier, permite utilizatorilor
# să adauge evaluări noi și scrie datele actualizate înapoi în fișier.
def citeste_filme_din_fisier(nume_fisier):
    filme = {}
    try:
        with open(nume_fisier, 'r') as f:
            for linie in f:
                titlu, evaluare = linie.strip().rsplit(',', 1)
                filme[titlu] = int(evaluare)
    except FileNotFoundError:
        print(f"Fișierul '{nume_fisier}' nu a fost găsit. Va fi creat automat la salvare.")
    return filme

def scrie_filme_in_fisier(nume_fisier, filme):
    with open(nume_fisier, 'w') as f:
        for titlu, evaluare in filme.items():
            f.write(f"{titlu}, {evaluare}\n")

def afiseaza_filme(filme):
    if filme:
        filme_sortate = sorted(filme.items(), key=lambda item: item[1], reverse=True)
        print("\nLista de filme și evaluările acestora (sortate după evaluare):")
        for titlu, evaluare in filme_sortate:
            print(f"{titlu}: {evaluare}")
    else:
        print("\nNu există filme în listă.")

def adauga_film(filme):
    titlu = input("Introdu titlul filmului: ").strip()
    if titlu in filme:
        print("Acest film există deja în listă.")
    else:
        evaluare = obtine_evaluare_valida()
        filme[titlu] = evaluare
        print(f"Film '{titlu}' adăugat cu evaluarea {evaluare}.")

def actualizeaza_evaluare(filme):
    titlu = input("Introdu titlul filmului de actualizat: ").strip()
    if titlu in filme:
        evaluare = obtine_evaluare_valida()
        filme[titlu] = evaluare
        print(f"Evaluarea filmului '{titlu}' a fost actualizată la {evaluare}.")
    else:
        print(f"Filmul '{titlu}' nu există în listă.")

def sterge_film(filme):
    titlu = input("Introdu titlul filmului de șters: ").strip()
    if titlu in filme:
        del filme[titlu]
        print(f"Filmul '{titlu}' a fost șters din listă.")
    else:
        print(f"Filmul '{titlu}' nu există în listă.")

def obtine_evaluare_valida():
    while True:
        try:
            evaluare = int(input("Introdu evaluarea (1-5): ").strip())
            if 1 <= evaluare <= 5:
                return evaluare
            else:
                print("Evaluarea trebuie să fie între 1 și 5.")
        except ValueError:
            print("Evaluarea trebuie să fie un număr întreg.")

def meniu():
    print("\nSistem de Evaluare a Filmelor")
    print("1. Vizualizează toate filmele și evaluările acestora")
    print("2. Adaugă un nou film și o evaluare")
    print("3. Actualizează evaluarea unui film existent")
    print("4. Șterge un film din listă")
    print("5. Salvează și ieși")

if __name__ == "__main__":
    nume_fisier = "movies.txt"
    filme = citeste_filme_din_fisier(nume_fisier)

    while True:
        meniu()
        optiune = input("\nAlege o opțiune (1-5): ").strip()
        if optiune == '1':
            afiseaza_filme(filme)
        elif optiune == '2':
            adauga_film(filme)
        elif optiune == '3':
            actualizeaza_evaluare(filme)
        elif optiune == '4':
            sterge_film(filme)
        elif optiune == '5':
            scrie_filme_in_fisier(nume_fisier, filme)
            print("Modificările au fost salvate. La revedere!")
            break
        else:
            print("Opțiune invalidă. Te rog să alegi între 1 și 5.")


