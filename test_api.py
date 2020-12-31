import requests



class TestApi:
    def __init__(self):
        self.user_url = "http://127.0.0.1:8000/auth/"
        self.user_profile_url = "http://127.0.0.1:8000/auth/users/"
        self.user_profile_data = "http://127.0.0.1:8000/api/accounts/"

        self.user_data = {
            'username': 'ibrahim',
            'password': 'adminmaster'
        }

    def create_user(self):  
        "This is for creating the user"
        response = requests.post(self.user_url+"users/", data=self.user_data)
        return self.get_jwt_token(), print(response.json(), response.status_code, " Create User")
    
    
    def get_jwt_token(self):
        """This is the same as logging in, jwt creates a token for you, you send that
        token to self.check_user, this brings out the user's details that you can query
        that means, with those details you can only show that specific data to the user"""

        response = requests.post(self.user_url+"jwt/create/", data=self.user_data)
        
        return self.check_user(response.json()['access']), print(response.json(), response.status_code, "Get Token")

    def check_user(self, token):
        """ This brings out the data for the querying """

        headers = {
            'Authorization': "Bearer "+str(token)
        }
        response = requests.get(self.user_profile_url+"me/", headers=headers)
        
        return self.user_profile(str(response.json()['id']), headers), self.all_profiles(headers), print(response.json(), response.status_code, "check user")

    def user_profile(self, id, headers):

        response = requests.get(self.user_profile_data+"profile/"+str(1)+"/", headers=headers)
        return print(response.json(), response.status_code, "user profile")
    
    def all_profiles(self, headers):

        response = requests.get(self.user_profile_data+"all-profiles",headers=headers)
        return print(response.json(), response.status_code, "all profiles")

    

testing = TestApi()
testing.get_jwt_token()
