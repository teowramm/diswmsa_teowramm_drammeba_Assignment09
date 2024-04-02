
#car.py

import requests
import json

class Car:
    def __init__(self, apiKey):
        self.apiKey = apiKey # establishing instance of API key so we can use it in main.py
        self.modelUrls = { #creating our dictionary of car models called modelUrls
            'camry': 'https://api.api-ninjas.com/v1/cars?model=camry',
            'corolla': 'https://api.api-ninjas.com/v1/cars?model=corolla',
            'bmw': 'https://api.api-ninjas.com/v1/cars?model=bmw',
            'chevrolet': 'https://api.api-ninjas.com/v1/cars?model=chevrolet',
            'toyota': 'https://api.api-ninjas.com/v1/cars?model=toyota'

        }
        self.carModels = list(self.modelUrls.keys()) #getting dictionary keys from modelUrls dictionary
        
    def carInfo(self, model):
        apiUrl = f'https://api.api-ninjas.com/v1/cars?model={model}' #https://api-ninjas.com/api/cars example model
        response = requests.get(apiUrl, headers={'X-Api-Key': self.apiKey}) #https://api-ninjas.com/api/cars
        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        #https://www.geeksforgeeks.org/json-loads-in-python/
        #https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/?ref=ml_lbp
        #https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/?ref=ml_lbp
        else:
            return None
