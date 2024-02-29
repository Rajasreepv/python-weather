from dotenv import load_dotenv
import requests
import os
load_dotenv()
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
def getcurrentweather(city="kansas city"):
    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    # request_url=f'https://api.openweathermap.org/data/3.0/onecall?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data=requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("Get Current Weather Conditions")
    city=input("Enter city name")
    getcurrentweather(city)
    
