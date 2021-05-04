import web
import json
import requests
from dotenv import load_dotenv

urls = (

)

app = web.application(urls, globals())
r = requests.get('api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={REACT_APP_WEATHER_API_KEY}', auth=('USER', 'PASSWORD'))


class zipcode:
    def GET(self, unit, value):
        web.header('Content-Type', 'application/json') # text/xml
        z = zip({unit: float(value)})
        return z.toJSON()


class zip:


if __name__ == "__main__":
    app.run()
