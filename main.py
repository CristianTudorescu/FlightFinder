from datamanager import DataManager
from datetime import datetime, timedelta

dataManager = DataManager()
sheet_data = dataManager.getGoogleSheetData()

print(sheet_data)

# put 'TESTING' inside iata code
# for i in range (0,len(sheet_data['prices'])):
#     if 'iataCode' in sheet_data['prices'][i]:
#         dataManager.putIataCode(jsonData={'price': {'iataCode' : 'TESTING'}},id=sheet_data['prices'][i]['id'])
#     else:
#         dataManager.putIataCode(jsonData={'price': {'iataCode' : 'TESTING', 'lowestPrice' : 54}},id=sheet_data['prices'][i]['id'])

# replace TESTING with actual iataCode
# for i in range (0,len(sheet_data['prices'])):
#     iataCode = dataManager.getIataCode(cityName=sheet_data['prices'][i]['city'])
#     dataManager.putIataCode(jsonData={'price': {'iataCode' : iataCode }},id=sheet_data['prices'][i]['id'])

# print(sheet_data)


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=100)
# for destination in sheet_data['prices']:
#     flight = dataManager.check_flights(
#         'BUD',
#         destination["iataCode"],
#         from_time=tomorrow,
#         to_time=six_month_from_today
#     )

a = dataManager.check_flights(
        'BUD',
        'LON',
        from_time=tomorrow,
        to_time=six_month_from_today
)