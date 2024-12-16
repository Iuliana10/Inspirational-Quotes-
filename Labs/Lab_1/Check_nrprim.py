def este_numar_prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+2):
        return True
numar = int(input("Introduceti un numar pentru a verifica daca este prim:"))
if este_numar_prim(numar):
    print(f"{numar} este un numar prim.")
else:
    print(f"{numar} nu este un numar prim.")