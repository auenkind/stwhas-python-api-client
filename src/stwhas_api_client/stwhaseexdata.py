from .stwhaseexvalue import StwHasEexValue

class StwHasEexData:

    def __init__(self, jsonData = None):
        self.data:list[StwHasEexValue] = []
        self.unit = ""
        if jsonData != None:
            self.parse(jsonData)
        pass

    def fromJson(data):
        return StwHasEexData(data)
    
    def parse(self, jsonData):
        if jsonData["values"] is None:
            raise Exception("Invalid data")
        self.unit = jsonData['unit']
        for value in jsonData["values"]:
            self.data.append(StwHasEexValue.fromJson(value))