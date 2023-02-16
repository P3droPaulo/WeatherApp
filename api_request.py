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
            self.main = self.request['weather'][0]['main']
            self.visibility = self.request['visibility']

            self.data = {'city':self.city, 'celcius':self.celcius, 'description':self.description,
            'humidity':self.humidity, 'pressure':self.pressure, 'feels_like':self.feels_like,
            'main':self.main, 'visibility':self.visibility}

if __name__ == "__main__":
    app = WeatherRequest('Ouro Preto')
    print(app.request)