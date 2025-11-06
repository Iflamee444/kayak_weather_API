import pandas as pd
import plotly.express as px


# Créer la carte avec les 5 meilleurs villes niveau prochain météo

def get_map_weather():
    # Charger les top 5 villes avec leur score
    top_cities = pd.read_csv("output/top_cities.csv", sep=";")

    # Charger les coordonnées
    cities_coords = pd.read_csv("output/cities_fr.csv", sep=";")

    # Ajouter lat/lon au top_cities
    top_cities = top_cities.merge(cities_coords, on="city", how="left")

    # Créer la carte
    fig = px.scatter_mapbox(
        top_cities,
        lat="lat",
        lon="lon",
        hover_name="city",
        hover_data={"weather_score": True, "lat": False, "lon": False},
        size="weather_score",
        color="weather_score",
        color_continuous_scale="Viridis",
        zoom=5,
        mapbox_style="carto-positron",
    )

    fig.update_layout(
        title="Les bon villes",
        margin={"r":0,"t":30,"l":0,"b":0}
    )

    fig.show()