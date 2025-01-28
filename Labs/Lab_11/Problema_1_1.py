import pandas as pd

data = pd.read_csv('vanzari.csv')

data['Data'] = pd.to_datetime(data['Data'])

data['Luna'] = data['Data'].dt.month
data['Anul'] = data['Data'].dt.year

most_sold_products = data.groupby(['Anul', 'Luna', 'Produs'])['Cantitate'].sum().reset_index()


most_sold_products_per_month = most_sold_products.loc[most_sold_products.groupby(['Anul', 'Luna'])['Cantitate'].idxmax()]

print(most_sold_products_per_month)

most_sold_products_per_month.to_csv('cele_mai_vandute_pe_luna.csv', index=False)
