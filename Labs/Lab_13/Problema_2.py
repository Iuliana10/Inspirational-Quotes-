"""Scrie un script Python care automatizeaza procesul de procesare al unui fisier CSV. Scriptul va
citi un fisier CSV care contine o lista de comenzi (ex: produse, cantitati si preturi), va calcula valoarea
totala pentru fiecare comanda si va salva rezultatele intr-un alt fisier CSV."""

import csv
def process_orders(input_file, output_file):
    try:
        with open(input_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Adăugăm o nouă coloană pentru valoarea totală
            fieldnames = reader.fieldnames + ["Valoare totala"]

            orders = []
            for row in reader:
                try:
                    cantitate = int(row["Cantitate"])
                    pret_unitar = float(row["Pret unitar"])
                    valoare_totala = cantitate * pret_unitar
                    row["Valoare totala"] = round(valoare_totala, 2)
                    orders.append(row)
                except ValueError:
                    print(f"Eroare la procesarea liniei: {row}")
                    continue

        # Scriem datele procesate într-un nou fișier CSV
        with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(orders)

        print(f"Procesarea s-a încheiat. Rezultatele sunt salvate în '{output_file}'.")
    except FileNotFoundError:
        print(f"Fișierul '{input_file}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")


# Exemplu de utilizare
input_csv = "produse.csv"
output_csv = "comenzi_procesate.csv"
process_orders(input_csv, output_csv)
