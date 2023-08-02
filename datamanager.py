import requests
import json

from flight_data import FlightData


class DataManager:
    def _init_(self):
        self.url = 'https://api.sheety.co/47a812eb38824a0fd951a3913e46718f/copieAFișieruluiFlightDeals/prices'
        self.flightApiKey = 'n1FTfoML9-sNLW5nTTKRkox1k8teh7Fb'
        self.flightUrl = 'https://api.tequila.kiwi'
        self.TEQUILA_API_KEY = 'n1FTfoML9-sNLW5nTTKRkox1k8teh7Fb'
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

    def getGoogleSheetData(self):
        res = requests.get(self.url)
        resp = json.loads(res.text)
        return resp

    def putIataCode(self, jsonData, id):
        putUrl = f"{self.url}/{id}"
        r = requests.put(putUrl, json=jsonData)
        print(r.text)

    def getIataCode(self, cityName):
        url = "https://api.tequila.kiwi.com/locations/query?term={term}&limit=1"
        params = {'term': cityName}
        headers = {
            "apikey": f"{self.flightApiKey}",
            "Content-Type": "application/json"
        }

        response = requests.get(url.format(term=params["term"]), headers=headers)
        data = json.loads(response.text)
        print(data)
        return (data['locations'][0]['code'])

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": self.TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(
            url=f"{self.TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data