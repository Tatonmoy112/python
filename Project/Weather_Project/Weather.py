import requests
import json
import win32com.client

inform=input("Enter the city name: ")
url=f"http://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={inform}"
speaker=win32com.client.Dispatch("SAPI.SpVoice")

wea=requests.get(url)
weather=json.loads(wea.text)
print("------------------")
print(f"{weather["location"]["name"]} - {weather["current"]["temp_c"]} : {weather["current"]["temp_f"]}")
speaker.speak(f"Location name: {weather["location"]["name"]} - Celsius: {weather["current"]["temp_c"]} & Fahrenheit: {weather["current"]["temp_f"]}")