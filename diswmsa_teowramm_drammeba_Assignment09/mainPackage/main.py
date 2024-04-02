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


from carPackage.car import *

if __name__ == "__main__":
    
    model = input("Please enter your car model! : ")
    carData = Car.carInfo(Car, model) # calling carInfo method
    if carData:
        print("Here's the information about your car:")
        print(json.dumps(carData, indent=4)) #converting info to json string 
    else:
        print("Sorry, we could not find information on your car")