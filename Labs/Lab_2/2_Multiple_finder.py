#2. Multiple finder
def find_multiples(num, start, end):
    multiples = []
    for i in range(start, end + 1):
        if i % num == 0:
            multiples.append(i)
    return multiples
number = int(input("Introduceți numărul pentru care căutați multiplii: "))
range_start = int(input("Introduceți începutul intervalului: "))
range_end = int(input("Introduceți sfârșitul intervalului: "))

multiples = find_multiples(number, range_start, range_end)
print(f"Multiplii lui {number} între {range_start} și {range_end} sunt: {multiples}")