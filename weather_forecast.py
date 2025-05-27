import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv('data/weather.csv')
df['day'] = range(len(df))  


X = df[['day']]
y = df['temp']
model = LinearRegression()
model.fit(X, y)


future_days = np.array(range(len(df), len(df) + 7)).reshape(-1, 1)
future_temps = model.predict(future_days)


plt.plot(df['day'], df['temp'], label='Historical')
plt.plot(future_days, future_temps, label='Forecast', linestyle='--')
plt.title('Temperature Forecast')
plt.xlabel('Day Index')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
