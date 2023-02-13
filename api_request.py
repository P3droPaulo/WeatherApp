import requests

class WeatherRequest():
    def __init__(self, city, lang="pt-br"):
        self.city = city
        self.lang = lang

        self.API_KEY = '431184d81cc92171cee033a4fa4e305d'
        self.API_LINK = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&lang={self.lang}'

        self.request = requests.get(self.API_LINK).json()
        
        if self.request['cod'] == '404':
            self.error = 404
        else:
            self.error = 202
            self.celcius = int(self.request['main']['temp'] - 273.15)
            self.description = self.request['weather'][0]['description']
            self.humidity = self.request['main']['humidity']
            self.pressure = self.request['main']['pressure']
            self.feels_like = int(self.request['main']['feels_like'] - 273.15)

            self.weatherData = [self.city, self.celcius, self.description, self.humidity, self.pressure,
            self.feels_like]

if __name__ == "__main__":
    app = WeatherRequest('Ouro Preto')
    print(app.request)