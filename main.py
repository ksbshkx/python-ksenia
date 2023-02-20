import requests
city = "Moscow,RU"
appid = "36acfc180a15c7087a2a147f6e3899ea"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("city:", city)
print("weather description:", data['weather'][0]['description'])
print("temperature:", data['main']['temp'])
print("min temperature:", data['main']['temp_min'])
print("max temperature:", data['main']['temp_max'])
print("wind speed:", data['wind']['speed'])
print("visibility:", data['visibility'])

print()

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'run', 'APPID': appid})
data = res.json()
print("weather forecast for a week:")
for i in data['list']:
    print("date <", i['dt_txt'], "> \r\ntemperature <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nweather conditions <", i['weather'][0]['description'], ">")
    print("wind speed <", i['wind']['speed'], "> \r\nvisibility <", i['visibility'], ">")
    print("____________________________")
