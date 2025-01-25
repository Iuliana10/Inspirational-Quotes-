#Simularea și Analiza Pieței de Acțiuni
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)
days = 730  # 2 ani (365 zile * 2)
initial_price = 100  # Prețul inițial al acțiunii
mean_change = 0  # Media modificării procentuale zilnice
std_dev_change = 2  # Abaterea standard a modificării procentuale
daily_changes = np.random.normal(mean_change, std_dev_change, days) / 100


prices = [initial_price]
for change in daily_changes:
    prices.append(prices[-1] * (1 + change))
prices = prices[1:]  # Eliminăm prețul inițial redundant
dates = pd.date_range(start="2024-01-01", periods=days)
df = pd.DataFrame({
    "Data": dates,
    "Schimbare Zilnică (%)": daily_changes * 100,
    "Preț de Închidere": prices
})


df["Media Mobilă 30z"] = df["Preț de Închidere"].rolling(window=30).mean()
df["Media Mobilă 100z"] = df["Preț de Închidere"].rolling(window=100).mean()
df["Peste Media 100z"] = df["Preț de Închidere"] > df["Media Mobilă 100z"]

plt.figure(figsize=(14, 7))


plt.plot(df["Data"], df["Preț de Închidere"], label="Preț de Închidere", color="blue", alpha=0.7)

plt.plot(df["Data"], df["Media Mobilă 30z"], label="Media Mobilă 30 zile", color="orange", linestyle="--")
plt.plot(df["Data"], df["Media Mobilă 100z"], label="Media Mobilă 100 zile", color="green", linestyle="--")

plt.fill_between(df["Data"], df["Preț de Închidere"], df["Media Mobilă 100z"],
                 where=df["Peste Media 100z"], color="lightgreen", alpha=0.5, label="Peste Media 100 zile")


plt.title("Evoluția Prețului Acțiunilor și Mediile Mobile")
plt.xlabel("Data")
plt.ylabel("Preț de Închidere ($)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()
