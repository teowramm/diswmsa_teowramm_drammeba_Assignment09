#car.py

def carInfo(self, model):
        apiUrl = f'https://api.api-ninjas.com/v1/cars?model={model}'
        response = requests.get(apiUrl, headers={'X-Api-Key': self.apiKey})
        if response.status_code == requests.codes.ok:
            return json.loads(response.content)
        #https://www.geeksforgeeks.org/json-loads-in-python/
        #https://www.geeksforgeeks.org/how-to-parse-data-from-json-into-python/?ref=ml_lbp
        #https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/?ref=ml_lbp
        else:
            return None