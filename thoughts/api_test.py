import requests


class TestAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/thoughts/"
        self.account_url = "http://127.0.0.1:8000/api/accounts/"
        self.username = "mitchel"
        self.password = "adminmaster"
        self.email = "mitchelinajuo@gmail.com"

        self.data = {
            "username": str(self.username),
            "password": str(self.password),
            "email": str(self.email),
        }

        self.headers = {
            'Content-Type': 'application/json'
        }

    def create_thoughts(self):
        data={
            'content':"This is my first thought, i hope you like it",
        }
        url = self.url

        response = requests.post(url, data=data)
        return print(response.json(), response.status_code)


testing = TestAPI()

testing.create_thoughts()
