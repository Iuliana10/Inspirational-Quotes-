def odd_or_even(number):
    if number % 2 == 0:
        return f"{number} este par."
    else:
        return f"{number} este impar."

try:
    number = int (input("introduceti un nr:"))
    result = odd_or_even(number)
    print(f"Numarul {number} este {result}.")
except ValueError:
    print("Te rog sa introduci un nr intreg valid")
    