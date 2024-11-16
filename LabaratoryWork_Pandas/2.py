import pandas as pd
import matplotlib.pyplot as plt

file_path = 'flights.csv'

df = pd.read_csv(file_path)

sorted_data = df.groupby('CARGO').agg(
    total_flights=('CARGO', 'size'),
    total_price=('PRICE', 'sum'),
    total_weight=('WEIGHT', 'sum')
).reset_index()

print(sorted_data)

plt.figure(figsize=(10, 6))
plt.bar(sorted_data['CARGO'], sorted_data['total_flights'], color='red')
plt.title('Flights have done by companies')
plt.xlabel('Company')
plt.ylabel('Total flights')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('1.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(sorted_data['CARGO'], sorted_data['total_price'], color='green')
plt.title('Total prices for each company')
plt.xlabel('Company')
plt.ylabel('Total price')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('2.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(sorted_data['CARGO'], sorted_data['total_weight'], color='blue')
plt.title('Total weight for each company')
plt.xlabel('company')
plt.ylabel('Total weight')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('3.png')
plt.show()
