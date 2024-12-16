#2.
def calculeaza_factorial(numar):
    if numar < 0:
        return "Factorialul nu este definit pentru numere negative."
    elif numar == 0 or numar == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, numar + 1):
            factorial *= i
        return factorial

try:
    numar = int(input("Introdu un număr pentru care să calculezi factorialul: "))
    rezultat = calculeaza_factorial(numar)
    print(f"Factorialul lui {numar} este: {rezultat}")
except ValueError:
    print("Te rog să introduci un număr întreg valid!")