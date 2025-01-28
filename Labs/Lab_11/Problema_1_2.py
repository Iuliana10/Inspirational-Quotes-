import pandas as pd

data = pd.read_csv('vanzari.csv')

data['Venit'] = data['Cantitate'] * data['Pret']

total_revenue_per_product = data.groupby('Produs')['Venit'].sum().reset_index()

total_revenue_per_product = total_revenue_per_product.sort_values(by='Venit', ascending=False)

print(total_revenue_per_product)

total_revenue_per_product.to_csv('venit_total_pe_produs.csv', index=False)
