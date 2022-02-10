from urllib import response
import requests
import datetime

class CBU():

    def __init__(self, v):
        date = datetime.datetime.now()
        y = date.year
        m = date.month
        d = date.day        
        url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/{v}/{y}-{m}-{d}/"
        response = requests.get(url)
        self.result = response.json()[0] 
        