boston = datasets.load_boston()
plt.scatter (boston_df["PRICE"], boston_df["TAX"], color='red'), plt.xlabel ("Цена хаты"), plt.ylabel ("Нологи")

plt.bar (boston_df["PRICE"], boston_df["INDUS"], color='green'), plt.xlabel('Цена'), plt.ylabel('Количество индусов поблизости')
