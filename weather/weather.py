import requests
import config

API_KEY = config.API_KEY

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    r = requests.get(base_url, params=params)
    if r.status_code == 200:
        data = r.json()
        print("\nWeather in:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Condition:", data["weather"][0]["description"])
    else:
        print("\nError:", r.json().get("message"))

def main():
    while True:
        city = input("Enter city name (or 'exit'): ")
        if city.lower() == "exit":
            break
        get_weather(city)

if __name__ == "__main__":
    main()
