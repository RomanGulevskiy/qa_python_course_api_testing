import requests


class OpenBreweryDBClient:

    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1/breweries"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_list_of_all_breweries(self):
        response = self.session.get(url=self.base_url)
        return response

    def get_random_brewery(self):
        response = self.session.get(url=f"{self.base_url}/random")
        return response

    def get_list_of_breweries_by_type(self, brewery_type):
        params = {"by_type": brewery_type}
        response = self.session.get(url=self.base_url, params=params)
        return response

    def get_list_of_breweries_by_city(self, city):
        params = {"by_city": city}
        response = self.session.get(url=self.base_url, params=params)
        return response

    def get_brewery_by_id(self, brewery_id_):
        response = self.session.get(url=f"{self.base_url}/{brewery_id_}")
        return response
