import math
def distanta_dintre_puncte(x1, y1, x2, y2):
    #A(x1, y1) și B(x2, y2)
    distanta = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distanta
try:
    x1 = float(input("Introdu coordonata x1: "))
    y1 = float(input("Introdu coordonata y1: "))
    x2 = float(input("Introdu coordonata x2: "))
    y2 = float(input("Introdu coordonata y2: "))

    rezultat = distanta_dintre_puncte(x1, y1, x2, y2)
    print(f"Distanța dintre punctele ({x1}, {y1}) și ({x2}, {y2}) este: {rezultat:.2f}")
except ValueError:
    print("Te rog să introduci valori numerice valide!")