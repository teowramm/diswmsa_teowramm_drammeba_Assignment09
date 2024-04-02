# Name: Mikaela Teowratanakul, Morgan Ferris, Smita Magar, Binta Drammeh
# email: teowramm@mail.uc.edu, ferrismb@mail.uc.edu, diswamsa@mail.uc.edu, drammeba@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/04/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Display your understanding of collaboration on Github and Eclipse, using APIs properly, creating the proper architecture (segregating modules into logical packages)
# Brief Description of what this module does: Displays our understanding of collaboration on Github and Eclipse, using APIs properly, creating the proper architecture (segregating modules into logical packages)
# Citations:
# In class work on 03/28.
# “Cars API.” Cars API - API Ninjas, api-ninjas.com/api/cars. 
#    Accessed 2 Apr. 2024. 
# GfG. “Convert JSON to Dictionary in Python.” GeeksforGeeks, GeeksforGeeks, 23 Aug. 2023, 
#     www.geeksforgeeks.org/convert-json-to-dictionary-in-python/?ref=ml_lbp. 
# GfG. “How to Parse Data from JSON into Python?” GeeksforGeeks, GeeksforGeeks, 5 July 2021, 
#     www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/?ref=ml_lbp. 
# GfG. “Json.Dumps() in Python.” GeeksforGeeks, GeeksforGeeks, 25 Oct. 2022, 
#     www.geeksforgeeks.org/json-dumps-in-python/. 
# Anything else that's relevant: N/A

import requests
import json

class Car:
    def __init__(self):
        self.modelTypes = { #creating our dictionary of car models called modelTypes
            'camry': 'https://api.api-ninjas.com/v1/cars?model=camry',
            'corolla': 'https://api.api-ninjas.com/v1/cars?model=corolla',
            'bmw': 'https://api.api-ninjas.com/v1/cars?model=bmw',
            'chevrolet': 'https://api.api-ninjas.com/v1/cars?model=chevrolet',
            'toyota': 'https://api.api-ninjas.com/v1/cars?model=toyota'
        }
        self.carModels = list(self.modelTypes.keys()) #getting dictionary keys from modelTypes dictionary
        
    def carInfo(self,model): # creating method so we can call it in the main
        apiUrl = f'https://api.api-ninjas.com/v1/cars?model={model}' # string literal for example models
        response = requests.get(apiUrl, headers={'X-Api-Key': 'VbX0aQXRm85Hr/exSWeRlA==z1tq1gt6z3OUe1oc'}) #from API ninjas example (our API's website description), using our API key
        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        else:
            return None
