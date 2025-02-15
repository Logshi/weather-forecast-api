import requests
import os
import json
# OpenWeatherMap API anahtarını buraya ekle (Buraya kendi API anahtarını eklemelisin)
API_KEY = "ab5896abe6334d7aa0046311e49d60f8"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        formatted_data = {
            "city": data["name"],
            "temperature (°C)": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "humidity (%)": data["main"]["humidity"],
            "wind_speed (m/s)": data["wind"]["speed"]}
        return formatted_data
    else:
        print(f"API isteği başarısız! Status Code: {response.status_code}")
        print(f"Hata Mesajı: {response.text}")
        return None

if __name__ == "__main__":
    city = "Berlin"
    data = get_weather(city)
    
    if data:
        print(json.dumps(data, indent=4, ensure_ascii=False))  # JSON formatında temiz çıktı
    else:
        print("Veri alınamadı!")