# main.py

from carPackage.car import *

if __name__ == "__main__":
    
    apiKey = 'VbX0aQXRm85Hr/exSWeRlA==z1tq1gt6z3OUe1oc' # API key needed for access
    carApi = Car(apiKey) # constructor call of Car class
    model = input("Please enter your car model! : ")
    carData = carApi.carInfo(model) # calling CarInfo method, connecting api key to URL
    if carData:
        print("Here's the information about your car:")
        print(json.dumps(carData, indent=4)) #converts to json string https://www.geeksforgeeks.org/json-dumps-in-python/
    else:
        print("Sorry, we could not find information on your car")