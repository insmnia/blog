import requests


class Blogger(object):
    
    def __repr__(self):
        return f'<{self.login}>'
    
    def get_user_info(self,id):
        return requests.get(f'http://localhost:5000/api/users/{id}')

    def get_user_followers(self,id):
        return requests.get(f'http://localhost:5000/api/users/{id}/followers')

    def get_user_followed(self,id):
        return requests.get(f'http://localhost:5000/api/users/{id}/followed')

    def create_user(self,login,password,email,about_me=None):
        return requests.post(
            'http://localhost:5000/api/users',data={
                                                "username":login,
                                                'password': password,
                                                'email':email,
                                                'about_me'=about_me
                                                }
        )