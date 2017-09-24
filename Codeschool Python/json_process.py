import requests

# https://home.openweathermap.org/api_keys pwd = openweathermap

url = "http://api.openweathermap.org/data/2.5/weather?q=Wilmette,fl&units=imperial&appid=6f2066b707f5ff565faf77fa1383aa31"
request = requests.get(url)

weather_json = request.json()
print(weather_json)
name = weather_json['name']
temp = weather_json['main']['temp']
print(temp)
print('The temperature in {} is {}'.format(name, temp))
# print(weather_json['dt'])