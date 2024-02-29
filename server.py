from flask import Flask,render_template,request
from weather import getcurrentweather
from waitress import serve

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)
def index():
    return render_template('index.html')
@app.route('/weather')
def getweather():
    city=request.args.get('city')
    weatherdata=getcurrentweather(city)
    
    if not weatherdata['cod'] == 200:
        return render_template("not-found.html")
    temp_max_celsius = fahrenheit_to_celsius(weatherdata['main']['temp_max'])
    feels_like_celsius = fahrenheit_to_celsius(weatherdata['main']['feels_like'])
    return render_template("weather.html",
    title= weatherdata["name"],
    status= weatherdata["weather"][0]["description"],
    temp= temp_max_celsius,
  feels_like = feels_like_celsius"


    )
if __name__ == "__main__":
    serve(app,host="0.0.0.0",port=3000)
