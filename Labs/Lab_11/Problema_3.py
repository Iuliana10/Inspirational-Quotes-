import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)


zile = 60
produse_min = 5
produse_max = 15
pret_medie = 40
dev_std_pret = 8
cantitate_min = 1
cantitate_max = 10
probabilitate_promotie = 0.3
discount_promotie = 0.2
marja_profit = 0.3


date = []

for zi in range(1, zile + 1):
    numar_produse = np.random.randint(produse_min, produse_max + 1)
    preturi = np.random.normal(pret_medie, dev_std_pret, numar_produse).clip(
        min=1)  # Asigurăm că nu sunt prețuri negative
    cantitati = np.random.randint(cantitate_min, cantitate_max + 1, numar_produse)


    promotii = np.random.rand(numar_produse) < probabilitate_promotie
    preturi_discount = np.where(promotii, preturi * (1 - discount_promotie), preturi)


    vanzari = preturi_discount * cantitati
    vanzari_totale = vanzari.sum()
    profit_total = vanzari_totale * marja_profit


    for produs in range(numar_produse):
        date.append({
            'Zi': zi,
            'Produs': produs + 1,
            'Pret Initial': preturi[produs],
            'Pret Discount': preturi_discount[produs],
            'Cantitate Vanduta': cantitati[produs],
            'Vanzari': vanzari[produs],
            'Promotie Aplicata': promotii[produs]
        })


df = pd.DataFrame(date)


df['Profit'] = df['Vanzari'] * marja_profit

totaluri_zilnice = df.groupby('Zi').agg(
    Vanzari_Totale=('Vanzari', 'sum'),
    Profit_Total=('Profit', 'sum')
).reset_index()


statistici = {
    'Pret': {
        'Medie': df['Pret Discount'].mean(),
        'Maxim': df['Pret Discount'].max(),
        'Minim': df['Pret Discount'].min()
    },
    'Cantitate': {
        'Medie': df['Cantitate Vanduta'].mean(),
        'Maxim': df['Cantitate Vanduta'].max(),
        'Minim': df['Cantitate Vanduta'].min()
    },
    'Profit': {
        'Medie': totaluri_zilnice['Profit_Total'].mean(),
        'Maxim': totaluri_zilnice['Profit_Total'].max(),
        'Minim': totaluri_zilnice['Profit_Total'].min()
    },
    'Vanzari Totale': totaluri_zilnice['Vanzari_Totale'].sum(),
    'Profit Total': totaluri_zilnice['Profit_Total'].sum()
}


plt.figure(figsize=(12, 6))
plt.plot(totaluri_zilnice['Zi'], totaluri_zilnice['Vanzari_Totale'], label='Vanzari Totale', marker='o')
plt.plot(totaluri_zilnice['Zi'], totaluri_zilnice['Profit_Total'], label='Profit Total', marker='o')
plt.title('Evolutia Veniturilor si a Profitului pe Zile')
plt.xlabel('Zi')
plt.ylabel('Suma (RON)')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(12, 6))
plt.hist(df['Pret Discount'], bins=20, alpha=0.7, label='Preturi Discount', color='blue')
plt.axvline(df['Pret Discount'].mean(), color='red', linestyle='--',
            label=f'Media Preturilor: {df["Pret Discount"].mean():.2f}')
plt.title('Distribuția Preturilor Discount')
plt.xlabel('Pret (RON)')
plt.ylabel('Frecventa')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(df['Cantitate Vanduta'], bins=10, alpha=0.7, label='Cantitati Vandute', color='green')
plt.axvline(df['Cantitate Vanduta'].mean(), color='red', linestyle='--',
            label=f'Media Cantitatilor: {df["Cantitate Vanduta"].mean():.2f}')
plt.title('Distribuția Cantităților Vândute')
plt.xlabel('Cantitate')
plt.ylabel('Frecventa')
plt.legend()
plt.grid(True)
plt.show()


zile_promotii = df[df['Promotie Aplicata']].groupby('Zi').agg(
    Impact_Promotie=('Pret Discount', 'mean'),
    Total_Promotii=('Promotie Aplicata', 'sum')
).reset_index()

plt.figure(figsize=(12, 6))
plt.bar(zile_promotii['Zi'], zile_promotii['Total_Promotii'], color='orange', alpha=0.7, label='Total Promotii')
plt.title('Numarul de Promotii pe Zi')
plt.xlabel('Zi')
plt.ylabel('Numar Promotii')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(zile_promotii['Zi'], zile_promotii['Impact_Promotie'], color='purple', marker='o', label='Pret Mediu Discount')
plt.title('Impactul Promoțiilor asupra Preturilor pe Zile')
plt.xlabel('Zi')
plt.ylabel('Pret Mediu Discount (RON)')
plt.legend()
plt.grid(True)
plt.show()


print("Dataset (primele 5 randuri):")
print(df.head())
print("\nTotaluri Zilnice (primele 5 zile):")
print(totaluri_zilnice.head())
print("\nStatistici Generale:")
for cheie, valoare in statistici.items():
    print(f"{cheie}: {valoare}")
