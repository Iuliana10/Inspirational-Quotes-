import math

num = int(input("Introdu un număr pentru a calcula rădăcina pătrată și factorialul: "))
angle = float(input("Introdu un unghi (în grade) pentru a calcula sinusul: "))

square_root = math.sqrt(num)
factorial = math.factorial(num)
sine_value = math.sin(math.radians(angle))

print(f"Rădăcina pătrată a {num} este {square_root}")
print(f"Factorialul lui {num} este {factorial}")
print(f"Sinusul unghiului de {angle} grade este {sine_value}")
