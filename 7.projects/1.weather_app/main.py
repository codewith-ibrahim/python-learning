import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
req = requests.get(url)

# print(req.text)
# print(type(req.text)) and its type is string now i want to convert it into dictionary.

weather_dict = json.loads(req.text)
temperature = weather_dict["current"]["temp_c"] #maine is dictionary mein sy temperature ko exract krliya hai.

print(f"The current temperature in {city} is {temperature}°C. Have a great day!")