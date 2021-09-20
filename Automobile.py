import pandas as pd
import matplotlib.pyplot as plt

# importing files
Automob=pd.read_csv("D:\Project 15\Data ssts\Automobile.csv")

# handle the missing values from price column

Automob['price']=Automob['price'].astype(float)

Automob['price']=Automob['price'].fillna(Automob['price'].mean())

#2. Get the values from Price column into a numpy.ndarray

price_numpy=Automob['price'].values
print(price_numpy)

# Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price

print(Automob['price'].max())

print(Automob['price'].min())

print(round(Automob['price'].mean(),3))

print(round(Automob['price'].std(),3))

#Make a pie chart for all car makers

series=Automob['make'].value_counts()

print(series)

carsmaker=series.index[0:12]

carscount=series.values[0:12]

plt.pie(carscount,labels=carsmaker,autopct='%.2f%%')

plt.show()
