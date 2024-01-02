from datetime import datetime
from datetime import timedelta
import json
from stwhasapiclient import StwHasApiClient, StwhasInterval


secrets = None
with open("secrets.json", "rt", encoding="utf-8") as sf:
    secrets = json.load(sf)

api = StwHasApiClient(secrets["username"], secrets["password"])

testtoken = secrets["testtoken"]

api.login()

end = datetime.now()
start = end - timedelta(days=1)

#eexdata = api.eexData(start, end, StwhasInterval.Hour, token=testtoken)
meterdata = api.smartMeterData(start, end, secrets["meternumber"], StwhasInterval.Hour)
print(meterdata)