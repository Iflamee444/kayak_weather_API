import pandas as pd
import plotly.express as px

def hotel_map_maker():
    top_cities = pd.read_csv("output/top_cities.csv", sep=";")
    cities_coords = pd.read_csv("output/cities_fr.csv", sep=";")
    hotels = pd.read_csv("output/hotels.csv", sep=";", names=["ville", "name", "rating"])


    hotels = hotels.merge(cities_coords, left_on="ville", right_on="city", how="left")
    hotels = hotels.merge(top_cities[["city", "weather_score"]], left_on="ville", right_on="city", how="left")

    hotels = hotels.dropna(subset=["rating"])
    hotels['rating'] = hotels['rating'].str.replace(",", ".", regex=False)
    hotels['rating'] = pd.to_numeric(hotels['rating'], errors='coerce')

    hotels = hotels.dropna(subset=['rating'])

    fig = px.scatter_mapbox(
        hotels,
        lat="lat",
        lon="lon",
        hover_name="name",
        hover_data={"ville": True, "rating": True, "lat": True, "lon": True},
        color="rating",
        size="rating",
        color_continuous_scale="Viridis",
        zoom=5,
        mapbox_style="carto-positron",
    )

    fig.update_layout(
        title="Les bon hôtels des bon villes",
        margin={"r":0,"t":30,"l":0,"b":0}
    )

    fig.show()
