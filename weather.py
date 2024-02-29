from dotenv import load_dotenv
import requests
import os
load_dotenv()

def getcurrentweather(city="kansas city"):
    
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=jZDF6fRrJ9GhfBR50Np3sg3QS3amHG4g"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.ok:
        # Parse the JSON response
        weather_data = response.json()
        return weather_data
    # request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    # weather_data=requests.get(request_url).json()
    # return weather_data

if __name__ == "__main__":
    print("Get Current Weather Conditions")
    city=input("Enter city name")
    getcurrentweather(city)
    
