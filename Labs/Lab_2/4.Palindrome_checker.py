#Palindrome checker
def este_palindrom(cuvant):
    cuvant = cuvant.lower().replace(" ", "")
    return cuvant == cuvant[::-1]

text = input("Introdu un cuvânt sau o frază: ")
if este_palindrom(text):
    print(" este un palindrom.", text)
else:
    print(" NU este un palindrom.", text)