import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ufo_sightings.csv')

print(df.head())
print(df.info())

df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['hour'] = df['datetime'].dt.hour

# df['shape'] = df['shape'].str.lower().str.strip()
# df['city'] = df['city'].str.lower().str.strip()
# df['country'] = df['country'].str.lower().str.strip()

year_counts = df['year'].value_counts().sort_index()
plt.figure()
year_counts.plot()

plt.title('UFO Sightings by Year')
plt.xlabel('Year')
plt.ylabel('Number of Sightings')
plt.grid()
plt.show()
