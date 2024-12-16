#1. Multiplication table generator
def tabel_inmultire(numar, limita):
    print("Tabelul de inmultire pentru: ", numar)
    for i in range(1, limita + 1):
        print(f"{numar} x {i} = {numar * i}")
try:
    numar = int(input("Introdu nr. pentru tabelul de inmultire: "))
    limita = int(input("Introdu limita pemtru tabel: "))
    tabel_inmultire(numar, limita)
except ValueError:
    print("Te rog sa introduci nr. intregi valide!")