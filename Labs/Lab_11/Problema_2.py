import numpy as np
import pandas as pd

np.random.seed(42)


days = 60
min_products = 5
max_products = 15
price_mean = 40
price_std_dev = 8
quantity_min = 1
quantity_max = 10
promotion_probability = 0.3
promotion_discount = 0.2
profit_margin = 0.3

data = []

for day in range(1, days + 1):
    num_products = np.random.randint(min_products, max_products + 1)
    prices = np.random.normal(price_mean, price_std_dev, num_products).clip(min=1)  # Ensure no negative prices
    quantities = np.random.randint(quantity_min, quantity_max + 1, num_products)


    promotions = np.random.rand(num_products) < promotion_probability
    discounted_prices = np.where(promotions, prices * (1 - promotion_discount), prices)


    sales = discounted_prices * quantities
    total_sales = sales.sum()
    total_profit = total_sales * profit_margin


    for product in range(num_products):
        data.append({
            'Day': day,
            'Product': product + 1,
            'Original Price': prices[product],
            'Discounted Price': discounted_prices[product],
            'Quantity Sold': quantities[product],
            'Sales': sales[product],
            'Promotion Applied': promotions[product]
        })


df = pd.DataFrame(data)


df['Profit'] = df['Sales'] * profit_margin


daily_totals = df.groupby('Day').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Profit', 'sum')
).reset_index()


stats = {
    'Price': {
        'Mean': df['Discounted Price'].mean(),
        'Max': df['Discounted Price'].max(),
        'Min': df['Discounted Price'].min()
    },
    'Quantity': {
        'Mean': df['Quantity Sold'].mean(),
        'Max': df['Quantity Sold'].max(),
        'Min': df['Quantity Sold'].min()
    },
    'Profit': {
        'Mean': daily_totals['Total_Profit'].mean(),
        'Max': daily_totals['Total_Profit'].max(),
        'Min': daily_totals['Total_Profit'].min()
    },
    'Total Sales': daily_totals['Total_Sales'].sum(),
    'Total Profit': daily_totals['Total_Profit'].sum()
}


print("Dataset (first 5 rows):")
print(df.head())
print("\nDaily Totals (first 5 days):")
print(daily_totals.head())
print("\nGeneral Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")
