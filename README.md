# weather app

A simple Python app that shows real-time weather using the [OpenWeatherMap API](https://openweathermap.org/api).  
You enter a city, and it returns the temperature, humidity, wind, and conditions.

---

# the features
- Search weather by city (supports `city,countrycode` like `paris,fr`)
- Displays:
  - Temperature (°C)  
  - Feels like temperature  
  - Humidity (%)  
  - Wind speed (m/s)  
  - Conditions (Clear, Clouds, Rain, etc.)
- Keeps your API key safe in a `.env` file (ignored by Git)

---

# setup

1. Clone the repo:
   ```bash
   git clone git@github.com:abnahomm/weather.app.git
   cd weather.app
