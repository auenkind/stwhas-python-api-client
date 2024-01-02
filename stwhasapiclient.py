from datetime import datetime
import json
from stwhasinterval import StwhasInterval
from stwhaseexdata import StwHasEexData
import requests

class StwHasApiClient:
    def __init__(self, username, password, endpoint= 'https://hassfurt.energy-assistant.de/api/') -> None:
        self.username = username
        self.password = password
        self.endpoint = endpoint
        self.token = None

    def login(self):
        loginData = {
            "email": self.username,
            "password": self.password
        }
        data = requests.post(self.endpoint + 'auth/v1/customer/login', json=loginData)
        if data.status_code == 200:
            self.token = data.json()["token"]
        print(self.token)

    def eexData(self, starttime:datetime, endtime:datetime, interval:StwhasInterval, token = None):
        url = "{endpoint}stockmarket/v1/mapped-values/startdate/{startdate}Z/enddate/{enddate}Z/interval/{interval}".format(
            endpoint=self.endpoint, 
            startdate=starttime.isoformat(), 
            enddate=endtime.isoformat(), 
            interval=interval.value)
        data = self.apiRequest(url, token).json()
        #data = json.loads('{"values":[{"datetime":"2024-01-01T22:00:00.000Z","price":0.01068,"interpolated":false},{"datetime":"2024-01-01T23:00:00.000Z","price":0.00244,"interpolated":false},{"datetime":"2024-01-02T00:00:00.000Z","price":0.030590000000000003,"interpolated":false},{"datetime":"2024-01-02T01:00:00.000Z","price":0.02007,"interpolated":false},{"datetime":"2024-01-02T02:00:00.000Z","price":0.031030000000000002,"interpolated":false},{"datetime":"2024-01-02T03:00:00.000Z","price":0.01839,"interpolated":false},{"datetime":"2024-01-02T04:00:00.000Z","price":0.011080000000000001,"interpolated":false},{"datetime":"2024-01-02T05:00:00.000Z","price":0.013779999999999999,"interpolated":false},{"datetime":"2024-01-02T06:00:00.000Z","price":0.04763,"interpolated":false},{"datetime":"2024-01-02T07:00:00.000Z","price":0.0581,"interpolated":false},{"datetime":"2024-01-02T08:00:00.000Z","price":0.06567,"interpolated":false},{"datetime":"2024-01-02T09:00:00.000Z","price":0.06473,"interpolated":false},{"datetime":"2024-01-02T10:00:00.000Z","price":0.06898,"interpolated":false},{"datetime":"2024-01-02T11:00:00.000Z","price":0.07354,"interpolated":false},{"datetime":"2024-01-02T12:00:00.000Z","price":0.07816,"interpolated":false},{"datetime":"2024-01-02T13:00:00.000Z","price":0.07887,"interpolated":false},{"datetime":"2024-01-02T14:00:00.000Z","price":0.07924,"interpolated":false},{"datetime":"2024-01-02T15:00:00.000Z","price":0.07996,"interpolated":false},{"datetime":"2024-01-02T16:00:00.000Z","price":0.08346,"interpolated":false},{"datetime":"2024-01-02T17:00:00.000Z","price":0.08092,"interpolated":false},{"datetime":"2024-01-02T18:00:00.000Z","price":0.07495,"interpolated":false},{"datetime":"2024-01-02T19:00:00.000Z","price":0.06318,"interpolated":false},{"datetime":"2024-01-02T20:00:00.000Z","price":0.05711,"interpolated":false},{"datetime":"2024-01-02T21:00:00.000Z","price":0.04689,"interpolated":false}],"unit":"€"}')
        return StwHasEexData.fromJson(data)
        
    def apiRequest(self, url, token):
        if token is None and self.token != None:
            token = self.token
        if token == None:
            raise Exception("Please Login first or provide token")
        
        return requests.get(url, headers={
            "Authorization": "Bearer "+token
        })