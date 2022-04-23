import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

n = df['Star_name']
d = df['Distance']
g = df['Gravity']
m = df['Mass']
r = df['Radius']

# Distance
plt.bar(n, d)
plt.show()

# Gravity
plt.bar(n, g)
plt.show()

# Mass
plt.bar(n, m)
plt.show()

# Radius
plt.bar(n, r)
plt.show()