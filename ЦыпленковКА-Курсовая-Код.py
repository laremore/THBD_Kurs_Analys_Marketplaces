import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
data = pd.read_csv("sales_data.csv")

# Преобразование даты
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Season'] = data['Month'].apply(lambda x: 'Winter' if x in [12, 1, 2]
                                       else 'Spring' if x in [3, 4, 5]
                                       else 'Summer' if x in [6, 7, 8]
                                       else 'Autumn')

# Установка цветовой схемы для постоянного использования
palette_regions = {"North America": "#1f77b4", "Europe": "#ff7f0e", "Asia": "#2ca02c"}
palette_categories = {"Electronics": "#1f77b4", "Home Appliances": "#ff7f0e", "Clothing": "#2ca02c",
                      "Books": "#d62728", "Beauty Products": "#9467bd", "Sports": "#8c564b"}
palette_payments = {"Credit Card": "#ff7f0e", "PayPal": "#1f77b4", "Debit Card": "#2ca02c"}
palette_seasons = {"Winter": "#1f77b4", "Spring": "#ff7f0e", "Summer": "#2ca02c", "Autumn": "#d62728"}

# Пункт 1: Наиболее популярный вид товаров в каждом из регионов
popular_products_region = data.groupby(['Region', 'Product Category'])['Units Sold'].sum().reset_index()
popular_products_region = popular_products_region.loc[popular_products_region.groupby('Region')['Units Sold'].idxmax()]
plt.figure(figsize=(10, 6))
sns.barplot(data=popular_products_region, x='Region', y='Units Sold', hue='Product Category', palette=palette_categories)
plt.title("Наиболее популярный вид товаров в каждом из регионов")
plt.xlabel("Регион")
plt.ylabel("Количество проданных товаров")
plt.legend(title='Категория товара')
plt.show()

# Пункт 2: Зависимость количества заказов от времени года (два графика)

# Первый график — количество заказов по месяцам
monthly_orders = data.groupby('Month')['Units Sold'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_orders, x='Month', y='Units Sold', marker='o', color="blue")
plt.title("Общее количество заказов по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Количество заказов")
plt.xticks(range(1, 13), ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'])
plt.show()

# Второй график — количество заказов по времени года с началом с зимы
seasonal_orders = data.groupby(['Season', 'Product Category'])['Units Sold'].sum().reset_index()
seasonal_orders['Season'] = pd.Categorical(seasonal_orders['Season'], ["Winter", "Spring", "Summer", "Autumn"])
plt.figure(figsize=(10, 6))
sns.barplot(data=seasonal_orders, x='Season', y='Units Sold', hue='Product Category', palette=palette_categories)
plt.title("Зависимость количества заказов от времени года")
plt.xlabel("Время года")
plt.ylabel("Количество заказов")
plt.legend(title='Категория товара')
plt.show()

# Пункт 3: Зависимость средней стоимости от региона
avg_price_region = data.groupby('Region')['Unit Price'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_price_region, x='Region', y='Unit Price', palette=palette_regions)
plt.title("Зависимость средней стоимости от региона")
plt.xlabel("Регион")
plt.ylabel("Средняя стоимость товара")
plt.show()

# Пункт 4: Наиболее популярный вид оплаты в каждом из регионов
popular_payment_region = data.groupby(['Region', 'Payment Method'])['Transaction ID'].count().reset_index()
popular_payment_region = popular_payment_region.loc[popular_payment_region.groupby('Region')['Transaction ID'].idxmax()]
plt.figure(figsize=(10, 6))
sns.barplot(data=popular_payment_region, x='Region', y='Transaction ID', hue='Payment Method', palette=palette_payments)
plt.title("Наиболее популярный вид оплаты в каждом из регионов")
plt.xlabel("Регион")
plt.ylabel("Количество транзакций")
plt.legend(title='Метод оплаты')
plt.show()

# Пункт 5: Вывод наиболее популярного способа оплаты для каждой категории (без графика)
popular_payment_category = data.groupby(['Product Category', 'Payment Method'])['Transaction ID'].count().reset_index()
popular_payment_category = popular_payment_category.loc[popular_payment_category.groupby('Product Category')['Transaction ID'].idxmax()]
print("Наиболее популярный метод оплаты для каждой категории товаров:")
print(popular_payment_category[['Product Category', 'Payment Method']])

# Пункт 6: Зависимость метода оплаты от цены
avg_price_payment = data.groupby('Payment Method')['Unit Price'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_price_payment, x='Payment Method', y='Unit Price', palette=palette_payments)
plt.title("Зависимость метода оплаты от цены")
plt.xlabel("Метод оплаты")
plt.ylabel("Средняя стоимость товара")
plt.show()

# Пункт 7: Зависимость количества, приобретенного за раз одним покупателем, от категории товара
quantity_category = data.groupby('Product Category')['Units Sold'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=quantity_category, x='Product Category', y='Units Sold', palette=palette_categories)
plt.title("Зависимость количества, приобретенного за раз, от категории товара")
plt.xlabel("Категория товара")
plt.ylabel("Среднее количество")
plt.xticks(rotation=90)
plt.show()

# Пункт 8: Зависимость средней стоимости от времени года
avg_price_season = data.groupby('Season')['Unit Price'].mean().reset_index()
avg_price_season['Season'] = pd.Categorical(avg_price_season['Season'], ["Winter", "Spring", "Summer", "Autumn"])
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_price_season, x='Season', y='Unit Price', palette=palette_seasons)
plt.title("Зависимость средней стоимости от времени года")
plt.xlabel("Время года")
plt.ylabel("Средняя стоимость товара")
plt.show()
