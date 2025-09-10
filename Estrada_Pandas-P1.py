import pandas as pd

cars = pd.read_csv("cars.csv")


print("First five rows of cars dataset:")
print(cars.head())

print("Last five rows of cars dataset:")
print(cars.tail())
