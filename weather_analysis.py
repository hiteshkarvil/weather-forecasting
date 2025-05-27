import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/weather.csv', parse_dates=['date'])

# Summary stats
print(df.describe())

# Plot temperature trend
plt.plot(df['date'], df['temp'], marker='o')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
