
v, f, t = input("Valoare, din, in: ").split()
print({"C": {"F": float(v) * 9/5 + 32, "K": float(v) + 273.15}, "F": {"C": (float(v) - 32) * 5/9, "K": (float(v) - 32) * 5/9 + 273.15}, "K": {"C": float(v) - 273.15, "F": (float(v) - 273.15) * 9/5 + 32}}[f][t])