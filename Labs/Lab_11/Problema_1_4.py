import pandas as pd

data = pd.read_csv('vanzari.csv')

data['Data'] = pd.to_datetime(data['Data'])

data['Venit'] = data['Cantitate'] * data['Pret']

data['Luna'] = data['Data'].dt.month
data['Anul'] = data['Data'].dt.year

venit_mediu_lunar = data.groupby(['Anul', 'Luna'])['Venit'].mean().reset_index()

print(venit_mediu_lunar)

venit_mediu_lunar.to_csv('venit_mediu_lunar.csv', index=False)
