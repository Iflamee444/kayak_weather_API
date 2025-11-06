import os
import pandas as pd
import requests as rq
import time

from settings import API_KEY, BASE_URL_OW_GEO, villes

from weather_city import get_city_weather
from best_city import best_cities
from map import get_map_weather
from hotels_list import get_hotel_per_city
from hotel_map import hotel_map_maker

csv_file = "output/cities_fr.csv"

def init_main_csv():
    if not os.path.exists(csv_file):
        df = pd.DataFrame(columns=["city", "lat", "lon"])
        df.to_csv(csv_file, index=False, sep=';')

    for ville in villes:
        params = {
            "q": f"{ville},FR",
            "limit": 1,
            "appid": API_KEY
        }
        response = rq.get(BASE_URL_OW_GEO, params=params)

        if response.status_code == 200:
            data = response.json()
            if data:
                info = data[0]
                lat = info.get("lat")
                lon = info.get("lon")

                # Append to CSV
                new_row = pd.DataFrame([{"city": ville, "lat": lat, "lon": lon}])
                new_row.to_csv(csv_file, mode='a', header=False, index=False, sep=';')

if __name__ == "__main__" :
    os.makedirs("output", exist_ok=True)
    init_main_csv()
    time.sleep(1.0)
    get_city_weather()
    time.sleep(1.0)
    best_cities()
    time.sleep(1.0)
    get_map_weather()
    time.sleep(1.0)
    get_hotel_per_city()
    time.sleep(1.0)
    hotel_map_maker()