from datetime import datetime

class StwHasEexValue:
    datetime:datetime = None
    price:float = 0.0
    interpolated:bool = False

    def __init__(self, jsonData = None):
        if jsonData != None:
            self.parse(jsonData)
        pass

    def fromJson(data):
        return StwHasEexValue(data)
    
    def parse(self, jsonData):
        self.datetime = datetime.fromisoformat(jsonData['datetime'], )
        self.price = jsonData['price']
        self.interpolated = jsonData['interpolated']