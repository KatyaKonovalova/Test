import pandas as pd
from ex_1 import df

# Задание: Вычислите остаток каждого из менеджеров на 01.07.2021.

df['receiving_date'] = pd.to_datetime(df['receiving_date'], errors='coerce')

# Фильтрация сделок, где оригиналы договоров получены после 30 июня 2021 года
remaining_deals = df.loc[
    (df['document'] == 'оригинал') &
    (df['receiving_date'] > '2021-06-30')
    ].copy()

# Расчет оставшегося бонуса для каждой сделки
remaining_deals['remaining_bonus'] = remaining_deals.apply(
    lambda row: 0.07 * row['sum'] if row['status'] == 'ОПЛАЧЕНО' else 0, axis=1
)

manager_remaining_bonus = remaining_deals.groupby('sale')['remaining_bonus'].sum()

if __name__ == "__main__":
    print('Остаток каждого менеджера на 01.07.2021:')
    print(manager_remaining_bonus.to_string(header=False))
