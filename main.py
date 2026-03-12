import pandas as pd
import folium

df = pd.read_csv("ufo_sightings.csv", low_memory=False)
# koordianti u brojeve
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df["city"] = df["city"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["shape"] = df["shape"].fillna("Unknown")


# brisanje redova sa nedostajućim koordinatama
df = df.dropna(subset=["latitude", "longitude"])

df = df.sample(5000)
# mapa
ufo_map = folium.Map(location=[20, 0], zoom_start=2)

# dodavanje markera
for index, row in df.iterrows():
    year = row["datetime"].year if pd.notnull(row["datetime"]) else "Unknown"
    popup_text = (
        f"<b>City:</b> {row['city']}<br>"
        f"<b>Country:</b> {row['country']}<br>"
        f"<b>Shape:</b> {row['shape']}<br>"
        f"<b>Year:</b> {year}"
    )
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=2,
        popup=folium.Popup(popup_text, max_width=200),
        tooltip=popup_text,
        color="red"
    ).add_to(ufo_map)
ufo_map.save("ufo_map.html")
