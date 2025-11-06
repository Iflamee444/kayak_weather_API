import pandas as pd

def best_cities():
    # Charger le fichier des scores météo
    df = pd.read_csv("output/cities_weather.csv", sep=";")

    # Supprimer les lignes avec valeurs manquantes (au cas où)
    df = df.dropna(subset=["weather_score"])

    # Trier par weather_score décroissant
    df_sorted = df.sort_values(by="weather_score", ascending=False)

    # Prendre les 5 premières villes
    top_5 = df_sorted.head(5)

    # Sauvegarder dans un nouveau CSV
    top_5.to_csv("output/top_cities.csv", sep=";", index=False)

    # print(top_5)
