def unique_pair_sum(numbers, target):
    seen = set()
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))  # Sortează pentru a asigura a <= b
            pairs.add(pair)
        seen.add(num)
    return pairs
numbers = list(map(int, input("Introduceți numerele separate prin spațiu: ").split()))
target = int(input("Introduceți valoarea țintă: "))
print(unique_pair_sum(numbers, target))
