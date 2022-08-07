import requests
from pprint import pprint
from config import weathertoken

def get_weather(city, weathertoken):
	try:
		r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weathertoken}&units=metric")
		data = r.json()
		pprint(data)

		city = data["name"]
		cur_weather = data["main"]["temp"]
		humidity = data["main"]["humidity"]
		pressure = data["main"]["pressure"]
		feels_like = data["main"]["feels_like"]
		wind = data["wind"]["speed"]
		if cur_weather >= 15.0:
			print("Сегодня особенно жарко")

		print(f"Погода в городе:{city}\nТемпература{cur_weather}\nОщущаеться как{feels_like}\nДавление{pressure} ветер {wind}")
	except Exception as ex:
		print(ex)

def main():
	city = input("Введите город: ")
	get_weather(city,weathertoken)

if __name__ == "__main__":
	main()