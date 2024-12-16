while True:
    char = input("Introduceti o litera: ")
    if char.isalpha():
        print("Ati introdus litera: ", char)
    else:
        print("Eroare! Ati introdus o cifra sau un caracter special.")
        break
