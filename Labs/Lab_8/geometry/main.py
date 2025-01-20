from circle import aria_cerc, circumferinta_cerc
from rectangle import aria_dreptunghi, perimetru_dreptunghi

# Exemplu de utilizare
raza = float(input("Introdu raza cercului: "))
lungime = float(input("Introdu lungimea dreptunghiului: "))
latime = float(input("Introdu lățimea dreptunghiului: "))

print(f"Aria cercului este: {aria_cerc(raza)}")
print(f"Circumferința cercului este: {circumferinta_cerc(raza)}")
print(f"Aria dreptunghiului este: {aria_dreptunghi(lungime, latime)}")
print(f"Perimetrul dreptunghiului este: {perimetru_dreptunghi(lungime, latime)}")
