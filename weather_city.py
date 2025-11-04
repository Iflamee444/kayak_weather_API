import pandas as pd
import requests as rq
import time
import os

API_KEY = "6f2adb4a3a5be330f97f688dc90405ac"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Param for API call : lat={lat}&lon={lon}&exclude={part}&appid={API key}

input_csv = "cities_fr.csv"
output_csv = "cities_weather.csv"

if not os.path.exists(output_csv):
    df = pd.DataFrame(columns=["city", "weather_score"])
    df.to_csv(output_csv, index =False, sep=';')

# Read the existing cities CSV
cities_df = pd.read_csv(input_csv, sep=';')

for _, row in cities_df.iterrows():
    city = row["city"]
    lat = row["lat"]
    lon = row["lon"]

    # print("Ville : %s \t Lat : %f \t Lon : %f" % (city, lat, lon))

    parametre = {
        "lat": lat,
        "lon": lon,
        "exclude": "minutely, hourly, daily, alerts",
        "appid": API_KEY,
        "units": "metric"
    }

    response = rq.get(BASE_URL,params=parametre,timeout=5)
    
    data = response.json()

    weather_scores = []
    for entry in data.get("list", []):
        main = entry.get("main", {})
        temp = main.get("temp")
        humidity = main.get("humidity")
        if temp is not None and humidity is not None:
            score = round(temp - (humidity / 10), 2)
            weather_scores.append(score)

            # print(data)
        else:
            pass

    if weather_scores:
        avg_score = round(sum(weather_scores) / len(weather_scores), 2)
    else:
        avg_score = None

    new_row = pd.DataFrame([{"city": city, "weather_score": avg_score}])
    new_row.to_csv(output_csv, mode='a', header=False, index=False, sep=';')

    time.sleep(1.2)