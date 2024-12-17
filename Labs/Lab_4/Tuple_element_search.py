#2.
input_lista = input("Introduceti elementele tuple-ului, separate prin spatii: ")
lista = input_lista.split()
tuplu = tuple(lista)
element_cautat = input("Introduceti elementul pe care doriti sa-l cautati: ")
if element_cautat in tuplu:
    print(f"Elementul '{element_cautat}' se află în tuple.")
else:
    print(f"Elementul '{element_cautat}' NU se află în tuple.")