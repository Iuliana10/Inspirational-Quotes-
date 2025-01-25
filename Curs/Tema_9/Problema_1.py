#Exercițiul 1: Analiza și Vizualizarea Datelor Meteo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)
zile = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
temperaturi = np.random.uniform(5, 35, size=len(zile))  # Temperaturi între 5°C și 35°C
umiditati = np.random.uniform(30, 90, size=len(zile))  # Umiditate între 30% și 90%
viteze_vant = np.random.uniform(0, 20, size=len(zile))  # Viteza vântului între 0 și 20 km/h


df = pd.DataFrame({
    "Data": zile,
    "Temperatura (°C)": temperaturi,
    "Umiditate (%)": umiditati,
    "Viteza Vântului (km/h)": viteze_vant
})

df["Temperatura Resimțită (°C)"] = df["Temperatura (°C)"] - 0.7 * (df["Umiditate (%)"] / 100)


zi_max_temp_resimtita = df.loc[df["Temperatura Resimțită (°C)"].idxmax()]
zi_min_temp_resimtita = df.loc[df["Temperatura Resimțită (°C)"].idxmin()]

print("Ziua cu cea mai mare temperatură resimțită:")
print(zi_max_temp_resimtita)
print("\nZiua cu cea mai mică temperatură resimțită:")
print(zi_min_temp_resimtita)


plt.figure(figsize=(12, 6))
plt.plot(df["Data"], df["Temperatura (°C)"], label="Temperatura (°C)", color="blue", alpha=0.7)
plt.plot(df["Data"], df["Temperatura Resimțită (°C)"], label="Temperatura Resimțită (°C)", color="red", alpha=0.7)
plt.title("Temperatura și Temperatura Resimțită pe Parcursul Anului")
plt.xlabel("Data")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


df["Luna"] = df["Data"].dt.month
temperatura_medie_lunara = df.groupby("Luna")["Temperatura (°C)"].mean()

plt.figure(figsize=(10, 5))
plt.bar(temperatura_medie_lunara.index, temperatura_medie_lunara, color="skyblue", alpha=0.8)
plt.title("Temperatura Medie Lunară")
plt.xlabel("Luna")
plt.ylabel("Temperatura Medie (°C)")
plt.xticks(range(1, 13), [
    "Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie",
    "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"
], rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

