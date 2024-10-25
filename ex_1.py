import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel-файла
file_path = './data.xlsx'
df = pd.read_excel(file_path)


# 1) Вычислите общую выручку за июль 2021 по тем сделкам, приход денежных средств которых не просрочен.

df['receiving_date'] = pd.to_datetime(df['receiving_date'], format='%d.%m.%y', errors='coerce')
july_data = df[(df['receiving_date'].dt.month == 7) & (df['receiving_date'].dt.year == 2021)]
total_revenue_july = july_data['sum'].sum()

df['month'] = df['receiving_date'].dt.to_period('M')
monthly_revenue = df.groupby('month')['sum'].sum()

# 2) Как изменялась выручка компании за рассматриваемый период? Проиллюстрируйте графиком.
monthly_revenue.plot(kind='bar', title='Изменение выручки по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка')


# 3) Кто из менеджеров привлек для компании больше всего денежных средств в сентябре 2021?
september_data = df[(df['receiving_date'].dt.month == 9) & (df['receiving_date'].dt.year == 2021)]
revenue_by_manager = september_data.groupby('sale')['sum'].sum()
top_manager = revenue_by_manager.idxmax()


# 4) Какой тип сделок (новая/текущая) был преобладающим в октябре 2021?
october_data = df[(df['receiving_date'].dt.month == 10) & (df['receiving_date'].dt.year == 2021)]
deal_type_count = october_data['new/current'].value_counts()


# 5) Сколько оригиналов договора по майским сделкам было получено в июне 2021?
june_data = df[(df['receiving_date'].dt.month == 6) & (df['receiving_date'].dt.year == 2021)]
original_count = june_data[june_data['document'] == 'оригинал'].shape[0]


if __name__ == "__main__":
    print(f'1. Общая выручка за июль 2021: {total_revenue_july}')
    print('2. График изменения выручки по месяцам')
    plt.show()
    print(f'3. Менеджер с наибольшей выручкой в сентябре 2021: {top_manager}')
    print(f'4. Преобладающий тип сделок в октябре 2021: {deal_type_count.idxmax()}')
    print(f'5. Количество оригиналов договоров, полученных в июне 2021: {original_count}')

