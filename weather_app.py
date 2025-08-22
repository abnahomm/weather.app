# weather_app.py
import os
import requests
from dotenv import load_dotenv

# load your api key from .env
load_dotenv()
api_key = os.getenv("owm_api_key", "").strip()

if not api_key:
    print("missing api key. put it in a .env file like: owm_api_key=YOUR_KEY")
    raise SystemExit(1)

base_url = "https://api.openweathermap.org/data/2.5/weather"

# adds emojis based off of the weather 
def mood(description: str) -> str:
    d = description.lower()
    if "thunder" in d: return "⛈️"
    if "drizzle" in d or "rain" in d: return "🌧️"
    if "snow" in d or "sleet" in d: return "❄️"
    if "clear" in d: return "☀️"
    if "cloud" in d: return "☁️"
    if "fog" in d or "mist" in d or "haze" in d: return "🌫️"
    return "🌍"

#  loop so you can check more than one city
# can also type things like paris, fr or london, uk
print("type a city (or just press enter to quit)")
while True:
    city = input("city: ").strip()
    if city == "":
        print("bye 👋")
        break

    # builds the url
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        # makes request
        res = requests.get(url, timeout=10)
        data = res.json()
    except Exception as e:
        print("network error:", e)
        continue

    
    if res.status_code == 200:
        main = data.get("main", {})
        temp = main.get("temp")
        feels = main.get("feels_like")
        humid = main.get("humidity")
        wind = data.get("wind", {}).get("speed")
        desc = (data.get("weather", [{}])[0].get("description", "")).title()
        face = mood(desc)

        print(f"\n{face}  weather in {city}:")
        if temp is not None:  print(f"temp: {temp}°c (feels like {feels}°c)")
        if humid is not None: print(f"humidity: {humid}%")
        if wind is not None:  print(f"wind: {wind} m/s")
        if desc:              print(f"conditions: {desc}")
        print()  # spacing here
    elif res.status_code == 401:
        # wrong api key or it isnt active
        msg = data.get("message", "invalid api key")
        print("api key issue:", msg)
        print("tip: verify email on openweathermap, wait a bit, or re-copy the key.")
    elif res.status_code == 404:
        # usually bad city name
        print("city not found. try again (you can do city,country like 'jacksonville,us').")
    else:
        # something else happened; show what they sent back
        print("error:", data.get("message", f"http {res.status_code}"))
