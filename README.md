Weather Monitoring System with Real-Time Data Processing
This project is a real-time weather monitoring system that fetches weather data from the OpenWeatherMap API at regular intervals, processes the data, stores it in an SQLite database, and triggers alerts based on user-defined thresholds.

Features
Real-time weather updates for Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
Temperature conversion from Kelvin to Celsius.
Daily weather summaries with maximum, minimum, and average temperatures.
Alerts when predefined weather conditions are met (e.g., high temperature or rain).
SQLite database integration for persistent storage of weather data.
Scheduling to fetch data every 5 minutes automatically.
Prerequisites
Python 3.x
SQLite3 (for database)
OpenWeatherMap API key:
Sign up for a free API key if you don't have one.
Setup Instructions
Clone the Repository

bash
Copy code
git clone <repository_url>
cd <repository_name>
Install Dependencies
Use the following command to install the necessary Python packages:

bash
Copy code
pip install requests pandas schedule
Get your OpenWeatherMap API Key

Sign up at OpenWeatherMap and get your free API key.
Create a Configuration File
In the root directory, create a file named config.py and add the following:

python
Copy code
API_KEY = "your_openweathermap_api_key"

# List of cities to monitor
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
Prepare the Database

Ensure the data/ folder exists:
bash
Copy code
mkdir -p data
You can create the SQLite database manually by running:
bash
Copy code
sqlite3 data/weather_data.db
Inside the SQLite shell, create the weather table:

sql
Copy code
CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    main TEXT,
    temp REAL,
    feels_like REAL,
    timestamp TEXT
);
Exit the SQLite shell:

bash
Copy code
.exit
How to Run the Application
Run the Application
Use the following command to start the weather monitoring system:

bash
Copy code
python weather_app.py
Expected Output
After running, you should see logs in the terminal:

kotlin
Copy code
Fetching weather data for Delhi...
{'city': 'Delhi', 'main': 'Clear', 'temp': 30.5, 'feels_like': 31.2, 'timestamp': 2024-10-19 15:45:00}
Weather data for Delhi saved to database.
ALERT! High temperature in Chennai - 36.1°C
Stop the Application
Use Ctrl + C to stop the system.

Design Choices
Scheduling with schedule Library:
The schedule library is used to fetch weather data every 5 minutes without blocking the main thread.

SQLite Database for Storage:
Weather data is stored in an SQLite database for later analysis and retrieval.

Error Handling:
The program gracefully handles network timeouts, invalid API keys, and missing data.

Alerts:
Alerts are triggered for:

Temperature > 35°C
Rain or Snow conditions
Code Structure
bash
Copy code
├── weather_app.py        # Main application file
├── config.py             # Configuration file for API key and city list
├── data/                 # Folder to store SQLite database
│   └── weather_data.db   # SQLite database
└── README.md             # Documentation
Test Cases
System Setup:

Verify that the system starts and connects to the OpenWeatherMap API with a valid API key.
Data Retrieval:

Simulate API calls at configurable intervals.
Ensure data is retrieved and parsed correctly.
Temperature Conversion:

Verify that temperatures are correctly converted from Kelvin to Celsius.
Daily Weather Summary:

Simulate multiple weather updates.
Check if the daily summaries (max, min, avg temperatures) are accurate.
Alerting Thresholds:

Configure thresholds (e.g., temp > 35°C).
Ensure alerts are triggered correctly when thresholds are exceeded.
Possible Improvements (Bonus)
Support for More Weather Parameters:
Add humidity, wind speed, etc., from the OpenWeatherMap API.
Weather Forecasts:
Fetch future weather predictions and generate forecasts.
Email or SMS Alerts:
Integrate with an email or SMS service to send notifications.
Known Issues
API Limits: Free OpenWeatherMap API keys have rate limits. Ensure you're within the allowed limits.
Network Connectivity: If the internet connection is unstable, the script may encounter timeouts.
License
This project is licensed under the MIT License.