#4.
text = input("Introduceti un text: ")
vocale = "aeiouăâîAEIOUĂÂÎ"
rezultat = "".join([litera for litera in text if litera not in vocale])
print("Textul fără vocale: ", rezultat)