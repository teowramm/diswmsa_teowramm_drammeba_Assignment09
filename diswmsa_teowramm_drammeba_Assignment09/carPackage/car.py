# car.py

import requests
import json

class Car:
    def __init__(self, apiKey):
        self.apiKey = apiKey # establishing instance of API key so we can use it in main.py
        self.modelUrls = { #creating our dictionary of car models called modelUrls
            'camry': 'https://api.api-ninjas.com/v1/cars?model=camry',
            'corolla': 'https://api.api-ninjas.com/v1/cars?model=corolla',
            'bmw': 'https://api.api-ninjas.com/v1/cars?model=bmw',
            'chevrolet': 'https://api.api-ninjas.com/v1/cars?model=chevrolet'
        }
        self.carModels = list(self.modelUrls.keys()) #getting dictionary keys from modelUrls dictionary
        