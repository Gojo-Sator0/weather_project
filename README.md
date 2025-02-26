![image](https://github.com/user-attachments/assets/136fc691-2827-4e09-ab89-b7b2c3cb52f8)Weather Forecast 🌦️

A Weather Forecast application built with Django, displaying current and forecasted weather for a selected city. 
The weather data is sourced using the OpenWeather API. The app also provides a temperature forecast chart for the next 24 hours.

Features:

  Search for weather by city name.
  Display current temperature, humidity, and pressure.
  Temperature forecast chart for the next 24 hours.

Requirements:
    Python 3.8+
    Django 5.1.3
    OpenWeather API key
    
Installation:

1.Clone the repository:
    git clone https://github.com/Gojo-Sator0/weather_project.git
    cd weather-app
2.Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate     # On Windows
3.Install dependencies:
    pip install -r requirements.txt
4.Configure the API key:
    Register at OpenWeather and obtain an API key.
    In the project’s settings file (e.g., settings.py), add your API key:
    WEATHER_API_KEY = 'your_openweather_api_key'
    
Running the Application:

1.Start the Django server:
    python manage.py runserver
2.Open your browser and go to **http://127.0.0.1:8000/weather/**.
3.Enter a city name to retrieve weather information and a temperature forecast chart.

Technologies Used:
    Django: Backend web framework.
    OpenWeather API: For fetching weather data.
    Matplotlib: For creating the temperature chart.

License
This project is licensed under the MIT License.

Authors
Vladimir Kulik - Application Development
