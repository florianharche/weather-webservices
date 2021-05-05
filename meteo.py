import web
import json
import requests
from dotenv import load_dotenv

load_dotenv()

urls = (
    '/(.*)', 'zipcode',
)

app = web.application(urls, globals())

class zipcode:
    def __init__(self,params):
        if len(params) == 1:
            web.header('Content-Type', 'application/json')
            r = requests.get('api.openweathermap.org/data/2.5/weather?zip={zip code}&appid=REACT_APP_WEATHER_API_KEY',
                             auth=('USER', 'PASSWORD'))
            data = r.json()
            #dictionnaire
            data = {
                "temp"
                "temp_min"
                "temp_max"
                "weather"
            }
        if len(params) != 1:
            raise Exception('Invalid ZIP code')
        return json.dumps(data)


if __name__ == "__main__":
    app.run()