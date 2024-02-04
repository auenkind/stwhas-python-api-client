from datetime import datetime, timezone
from datetime import timedelta
import json
from src.stwhas_api_client import StwHasApiClient, StwhasInterval, StwhasUnit
import os, time

print(datetime.now(timezone.utc).astimezone().tzinfo)

secrets = None
with open("secrets.json", "rt", encoding="utf-8") as sf:
    secrets = json.load(sf)

api = StwHasApiClient(secrets["username"], secrets["password"])

testtoken = secrets["testtoken"]

api.login()

end = datetime.utcnow().date()
end = datetime(end.year, end.month, end.day, tzinfo=timezone.utc)
start = end - timedelta(days=1)

#eexdata = api.eexData(start, end, StwhasInterval.Hour, token=testtoken)
#meterdata = api.smartMeterData(start, end, secrets["meternumber"], StwhasInterval.Hour)
#print(meterdata)

cost = api.consumptionCost(start, end, StwhasInterval.Hour, StwhasUnit.Kwh)
for row in cost.data:
    print(f"{row.time} {row.workprice} {row.sum} {row.delivery}")