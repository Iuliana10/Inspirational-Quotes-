
produse_preturi = {
    "mere": 2.5,
    "pere": 3.0,
    "banane": 1.8,
    "portocale": 2.2,
    "lapte": 5.0,
    "paine": 4.0
}
stoc_initial = {
    "mere": 10,
    "pere": 8,
    "banane": 15,
    "portocale": 7,
    "lapte": 12,
    "paine": 6
}
vanzari_zi = [
    ("mere", 4),
    ("pere", 3),
    ("banane", 6),
    ("portocale", 5),
    ("lapte", 2),
    ("paine", 3)
]
stoc_actualizat = stoc_initial.copy()
venit_total = 0
for produs, cantitate_vanduta in vanzari_zi:
    if produs in produse_preturi and produs in stoc_actualizat:
        cantitate_disponibila = stoc_actualizat[produs]
        cantitate_vanduta_efectiva = min(cantitate_vanduta, cantitate_disponibila)
        venit_total += produse_preturi[produs] * cantitate_vanduta_efectiva
        stoc_actualizat[produs] -= cantitate_vanduta_efectiva

produse_realimentare = {produs for produs, stoc in stoc_actualizat.items() if stoc < 5}
raport = {
    "Venit total": venit_total,
    "Stocuri ramase": stoc_actualizat,
    "Produse de realimentat": produse_realimentare
}
print("Raportul Zilnic:")
print(f"Venit total: {venit_total}")
print("Stocuri rămase:")
for produs, stoc in stoc_actualizat.items():
    print(f"  - {produs}: {stoc} bucăți")
print("Produse care trebuie realimentate:")
for produs in produse_realimentare:
    print(f"- {produs}")