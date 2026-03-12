import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium

# df['shape'] = df['shape'].str.lower().str.strip()
# df['city'] = df['city'].str.lower().str.strip()
# df['country'] = df['country'].str.lower().str.strip()

df = pd.read_csv('ufo_sightings.csv')

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
# Remove rows with invalid coordinates
df = df.dropna(subset=["latitude", "longitude"])

df = df.sample(5000)

ufo_map = folium.Map(location=[20, 0], zoom_start=2)
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=2,
        popup=row["city"],
        color="red"
    ).add_to(ufo_map)
ufo_map.save("ufo_map.html")
