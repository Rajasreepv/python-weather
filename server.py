# import math
# from flask import Flask,render_template,request
# from weather import getcurrentweather
# from waitress import serve

# app=Flask(__name__)
# def kelvin_to_celsius(kelvin):
#     celsius = kelvin - 273.15
#     return round(celsius, 2)
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')
# @app.route('/weather')
# def getweather():
#      city = request.args.get('city')
#      weatherdata = getcurrentweather(city)
    
#     if 'data' not in weatherdata or 'values' not in weatherdata['data']:
#         return render_template("not-found.html")

#     temperature_kelvin = weatherdata['data']['values']['temperature']
#     
    
#     return render_template("weather.html",
#                            title=weatherdata["location"]["name"],
#                            status=weatherdata["data"]["values"]["weatherCode"],
#                            temp=temperature_kelvin)
    # city=request.args.get('city')
    # weatherdata=getcurrentweather(city)
    # if not weatherdata['cod'] == 200:
    #     return render_template("not-found.html")
    
    # return render_template("weather.html",
                       
    # title= weatherdata["name"],
    # status= weatherdata["weather"][0]["description"],
    # temp = fahrenheit_to_celsius(weatherdata['main']['temp_max']),
    # feels_like = fahrenheit_to_celsius(weatherdata['main']['feels_like']))
  #   temp= f"{ weatherdata['main']['temp']:.1f}",
  # feels_like = f"{weatherdata['main']['feels_like']:.1f}"

import math
from flask import Flask, render_template, request
from weather import getcurrentweather
from waitress import serve

app = Flask(__name__)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def getweather():
    city = request.args.get('city')
    weatherdata = getcurrentweather(city)
    
    if 'data' not in weatherdata or 'values' not in weatherdata['data']:
        return render_template("not-found.html")
    latest_entry = weatherdata['timelines']['minutely'][-1]
    
    # temperature_kelvin = weatherdata['data']['values']['temperature']
    temperature_kelvin = latest_entry['values']['temperature']
    
    
    return render_template("weather.html",
                           title=weatherdata["location"]["name"],
                           status=weatherdata["data"]["values"]["weatherCode"],
                           temp=temperature_kelvin)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

    

