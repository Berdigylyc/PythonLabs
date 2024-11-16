import pandas as pd

file_path = 'transactions.csv'

df = pd.read_csv(file_path)

df_ok = df[df['STATUS'] == 'OK']

l_t_p = df_ok.nlargest(3, 'SUM')

print("Three largest payments:")
print(l_t_p[['CONTRACTOR', 'SUM']])

U_P = df_ok[df_ok['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum()

print(f"\n Umbrella totally payed: {U_P}")
