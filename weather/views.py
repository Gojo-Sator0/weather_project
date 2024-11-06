from django.shortcuts import render
import requests
import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.conf import settings

#127.0.0.1:8000/weather
#отправляет запрос в OpenWeatherMap API с указанием города и API ключа.
def get_weather_data(city): 
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'list' in data:
            return data
    return None

def weather_view(request):
    city = request.GET.get('city', 'London')  # Город по умолчанию
    data = get_weather_data(city)
    
    if data:
        # Извлекаем данные для первого прогноза
        temp = data['list'][0]['main']['temp']
        humidity = data['list'][0]['main']['humidity']
        pressure = data['list'][0]['main']['pressure']
        temp_chart = create_temp_chart(data)  # График
    else:
        temp = humidity = pressure = None
        temp_chart = None

    context = {
        'data': data,
        'city': city,
        'temp': temp,
        'humidity': humidity,
        'pressure': pressure,
        'temp_chart': temp_chart
    }
    return render(request, 'weather/weather.html', context)

# Функция для создания графика температуры
def create_temp_chart(data):
    if not data or 'list' not in data:
        return None

    temps = [item['main']['temp'] for item in data['list'][:8]]
    times = [item['dt_txt'] for item in data['list'][:8]]

    plt.figure(figsize=(10, 5))
    plt.plot(times, temps, marker='o', color='b')
    plt.title("Прогноз температуры на следующие 24 часа")
    plt.xlabel("Время")
    plt.ylabel("Температура (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return image_base64
