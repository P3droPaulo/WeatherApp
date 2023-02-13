from flask import Flask, render_template
from api_request import WeatherRequest
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    city_input = 'Rio de Janeiro'
    weather = WeatherRequest(city_input)

    if weather.error == 202:
        return render_template('homepage.html', city=weather.weatherData[0], temp=weather.weatherData[1],
        description=weather.weatherData[2], humidity=weather.weatherData[3], pressure=weather.weatherData[4],
        feels_like=weather.weatherData[5])
    elif weather.error == 404:
        return render_template('not_found.html')

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()