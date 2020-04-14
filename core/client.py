import requests
import json

class Client:

    def __init__(self):
        self.cookie = None
        try:
            with open ('../config.json') as f:
                self.config = json.loads(f.read())
        except FileNotFoundError:
            raise
        self.HOST = self.config['SERVER']['HOST']
        self.PORT = self.config['SERVER']['PORT']
        self.base_url = 'http://%s:%s/ipfs/'%(self.HOST, self.PORT)
        self.login_url = self.base_url + 'login'
        self.list_url = self.base_url + 'list'
        self.add_url = self.base_url + 'add'
        self.delete_url = self.base_url + 'delete'
        self.username = self.config['CLIENT']['USERNAME']
        self.password = self.config['CLIENT']['PASSWORD']
        self.login()

    def login(self):
        params = {
            "username": self.username,
            "password": self.password
        }
        try:
            res = requests.post(self.login_url, params)
            cookies = res.cookies
            print(res.text)
            self.cookie = requests.utils.dict_from_cookiejar(cookies)
            return True
        except Exception:
            return False

    def list_files(self):
        try:
            res = requests.get(self.list_url, cookies=self.cookie)
        except Exception:
            return None
        return json.loads(res.text).get('data')

    def add(self, **kwargs):
        try:
            res = requests.post(self.add_url, kwargs, cookies=self.cookie)
        except Exception:
            return None
        return json.loads(res.text).get('data')

    def delete(self, **kwargs):
        try:
            res = requests.post(self.delete_url, kwargs, cookies=self.cookie)
        except Exception:
            return None
        return json.loads(res.text).get('data')


