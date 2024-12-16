credit = float(input("Introduceti suma creditului: "))
rate = float(input("Introduceti rata dobanzii (in procente):"))
timp = float(input("Introduceti timpul in ani: "))
dobanda = (credit * rate * timp) / 100
print("Dobanda este: ", dobanda)
