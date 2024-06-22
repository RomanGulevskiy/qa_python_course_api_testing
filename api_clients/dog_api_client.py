import requests


class DogApiClient:

    def __init__(self,
                 base_url="https://dog.ceo/api"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_random_image(self):
        response = self.session.get(url=f"{self.base_url}/breeds/image/random")
        return response

    def get_images_by_breed(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/images")
        return response

    def get_list_of_subbreeds(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/list")
        return response

    def get_list_of_all_breeds(self):
        response = self.session.get(url=f"{self.base_url}/breeds/list/all")
        return response

    def get_random_image_from_breed_collection(self, breed):
        response = self.session.get(url=f"{self.base_url}/breed/{breed}/images/random")
        return response
