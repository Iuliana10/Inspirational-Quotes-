import pandas as pd
data = pd.read_csv('vanzari.csv')
data['Data'] = pd.to_datetime(data['Data'])

start_date = "01/01/2023"
end_date = "03/31/2023"


filtered_sales = data[(data['Data'] >= start_date) & (data['Data'] <= end_date)]

print(filtered_sales)

filtered_sales.to_csv('vanzari_filtrate.csv', index=False)
