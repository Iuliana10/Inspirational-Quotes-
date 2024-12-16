#3. Number guessing game
import random
def joc_ghicit_numar():
    print("Bine ai venit la Jocul de Ghicit Numere!")

    limita_inferioara = int(input("Introdu limita inferioară: "))
    limita_superioara = int(input("Introdu limita superioară: "))

    numar_secret = random.randint(limita_inferioara, limita_superioara)

    print(f"Am ales un număr între {limita_inferioara} și {limita_superioara}. Încearcă să-l ghicești!")

    incercari = 0
    ghicit = False


    while not ghicit:
        incercare = int(input("Introdu numărul tău: "))
        incercari += 1

        if incercare < numar_secret:
            print("Prea mic! Încearcă din nou.")
        elif incercare > numar_secret:
            print("Prea mare! Încearcă din nou.")
        else:
            print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
            ghicit = True
joc_ghicit_numar()