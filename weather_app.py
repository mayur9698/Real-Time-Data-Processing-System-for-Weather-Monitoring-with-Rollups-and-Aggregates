# weather_app.py

import requests
import pandas as pd
import schedule
import time
from datetime import datetime
from config import API_KEY, CITIES  # Import API key and city list from config.py
import sqlite3

# Function to get weather data from OpenWeatherMap API with error handling
def get_weather_data(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        print(f"Fetching weather data for {city}...")  # Debug log
        response = requests.get(url, timeout=10)  # Set a 10-second timeout

        if response.status_code != 200:
            print(f"Error fetching data for {city}: {response.status_code} - {response.text}")
            return None  # Stop further processing if there's an error

        data = response.json()

        # Extract relevant data
        weather = {
            "city": city,
            "main": data["weather"][0]["main"],
            "temp": data["main"]["temp"] - 273.15,  # Convert Kelvin to Celsius
            "feels_like": data["main"]["feels_like"] - 273.15,
            "timestamp": pd.to_datetime(data["dt"], unit='s')
        }
        return weather

    except requests.exceptions.Timeout:
        print(f"Request to {city} timed out.")
        return None  # Handle timeouts gracefully

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None  # Handle any other exceptions

# Function to save weather data to SQLite database (Optional)
def save_to_database(weather):
    if weather is None:
        print("No weather data to save.")
        return  # Skip saving if there's no valid weather data

    try:
        conn = sqlite3.connect("data/weather_data.db")
        df = pd.DataFrame([weather])
        df.to_sql("weather", conn, if_exists="append", index=False)
        conn.close()
        print(f"Weather data for {weather['city']} saved to database.")
    except Exception as e:
        print(f"Error saving to database: {str(e)}")

# Function to trigger alerts based on weather conditions
def check_alerts(weather):
    if weather is None:
        return  # Skip alerting if no data

    if weather["temp"] > 35:
        print(f"ALERT! High temperature in {weather['city']} - {weather['temp']}°C")

    if weather["main"] in ["Rain", "Snow"]:
        print(f"ALERT! {weather['main']} detected in {weather['city']}")

# Scheduler function to fetch weather data every 5 minutes
def fetch_and_store_weather():
    for city in CITIES:
        weather = get_weather_data(city)
        print(weather)  # Debug: Print the weather data
        save_to_database(weather)
        check_alerts(weather)

# Schedule the weather fetching function
schedule.every(5).minutes.do(fetch_and_store_weather)

# Run the scheduler with feedback
print("Starting weather monitoring system...")
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the weather monitoring system.")
        break
