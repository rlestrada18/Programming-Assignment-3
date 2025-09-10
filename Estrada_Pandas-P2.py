
import pandas as pd

cars = pd.read_csv("Cars.csv")

print("First five rows with odd-numbered columns:")
print(cars.iloc[:5, ::2])

print("\nRow containing 'Mazda RX4':")
print(cars[cars['Model'] == 'Mazda RX4'])

camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"\nCamaro Z28 has {camaro_cyl} cylinders.")

models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
print("\nCylinders and gear type for Mazda RX4 Wag, Ford Pantera L, and Honda Civic:")
print(subset)
