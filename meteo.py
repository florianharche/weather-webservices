import web
import json

urls = (
    '/([ckf])=(.*)', 'temperature',
    '/(.*)', 'error',
)
app = web.application(urls, globals())

class temperature:
    def GET(self, unit, value):
        web.header('Content-Type', 'application/json') # text/xml
        t = temp({unit: float(value)})
        return t.toJSON()

class temp:
    def __init__(self, params:dict):
        if len(params) is 0:
            raise Exception('Invalid Temperature')
        if len(params)> 1:
            raise Exception('Invalid Temperature, only one param to set !')
        self._temperatures = params
        if 'c' in self._temperatures:
            self.c_to_f()
            self.c_to_k()
        elif 'k' in self._temperatures:
            self.k_to_c()
            self.c_to_f()
        else:
            self.f_to_c()
            self.c_to_k()


    def c_to_k(self):
        self._temperatures['k'] = self._temperatures['c'] + 273.15

    def k_to_c(self):
        self._temperatures['c'] = self._temperatures['k'] - 273.15

    def f_to_c(self):
        self._temperatures['c'] = round((self._temperatures['f'] - 32) / 1.8, 2)

    def c_to_f(self):
        self._temperatures['f'] = self._temperatures['c'] * 1.8 + 32

    def toJSON(self):
        return json.dumps(self._temperatures)

    def __str__(self):
        return "<t><c>{}</c><f>{}</f><k>{}</k></t>".format(self._c, self._f, self._k)



if __name__ == "__main__":
    app.run()
