#1.
numere = input("Introduceți numerele separate prin spațiu: ")
lista_numere = [int(x) for x in numere.split()]
maxim = max(lista_numere)
minim = min(lista_numere)
print("Numărul maxim este:", maxim)
print("Numărul minim este:", minim)
