from flask import Flask, render_template
from api_request import WeatherRequest
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    city_input = 'Cachoeira do Campo'
    weatherRequest = WeatherRequest(city_input)

    img = weatherRequest.data['main']
    print(img)

    if weatherRequest.error == 202:
        return render_template('homepage.html', weatherData=weatherRequest.data,
        img=img)
    elif weatherRequest.error == 404:
        return render_template('not_found.html')

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()