import requests


class JSONPlaceholderClient:

    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_post_by_id(self, post_id):
        response = self.session.get(url=f"{self.base_url}/posts/{post_id}")
        return response

    def get_posts_by_user(self, user_id):
        params = {"userId": user_id}
        response = self.session.get(url=f"{self.base_url}/posts",
                                    params=params)
        return response

    def get_todo_by_id(self, todo_id):
        response = self.session.get(url=f"{self.base_url}/todos/{todo_id}")
        return response

    def get_photo_by_id(self, photo_id):
        response = self.session.get(url=f"{self.base_url}/photos/{photo_id}")
        return response

    def get_comments_by_post(self, post_id):
        response = self.session.get(url=f"{self.base_url}/posts/{post_id}/comments")
        return response

