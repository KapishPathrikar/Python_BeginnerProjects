import requests
import json
import pyttsx3

city = input("Enter the city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key=baed83c2066743eb9f3114109260306&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
text_to_speech = pyttsx3.init()
print(f"Temperature in {city} is {wdic['current']['temp_c']}°C")
text_to_speech.say(f"Temperature in {city} is {wdic['current']['temp_c']}°C")
text_to_speech.runAndWait()