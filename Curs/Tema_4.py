import re
def verifica_complexitate_parola(parola):
    criterii_neindeplinite = []
    if len(parola) < 8:
        criterii_neindeplinite.append("Lungimea trebuie să fie de cel puțin 8 caractere.")
    if not any(char.isupper() for char in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o literă majusculă.")
    if not any(char.islower() for char in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o literă minusculă.")
    if not any(char.isdigit() for char in parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin o cifră.")
    if not re.search(r"[!@#$%^&*()\-_=+<>?]", parola):
        criterii_neindeplinite.append("Trebuie să conțină cel puțin un caracter special (!@#$%^&*()-_+=<>?).")
    if " " in parola:
        criterii_neindeplinite.append("Nu trebuie să conțină spații.")
    if not criterii_neindeplinite:
        return "Parola este puternică!"
    else:
        return f"Parola este slabă. Probleme:\n" + "\n".join(criterii_neindeplinite)
parola = input("Introdu parola ta: ")
rezultat = verifica_complexitate_parola(parola)
print(rezultat)
