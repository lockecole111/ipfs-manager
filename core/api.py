import json
from .client import Client
from .ipfs import IPFS
import os

class Api:

    def __init__(self):
        try:
            with open ('config.json') as f:
                self.config = json.loads(f.read())
        except FileNotFoundError:
            raise
        self.DOWNLOAD_PATH = self.config['CLIENT']['DOWNLOAD_PATH']
        self.ipfs = IPFS(self.config)
        self.client = Client(self.config)
        self.files = self.client.list_files()
        self.client.login()

    def isLogin(self):
        return self.client.logined
    def isConnected(self):
        return self.client.connected    

    def login(self, username, password):
        self.client.username = username
        self.client.password = password
        self.client.login()

    def add(self, file_path):
        add_info = self.ipfs.add(file_path)
        hash = add_info['Hash']
        name = add_info['Name']
        size = add_info['Size']
        return self.client.add(name = name, hash = hash, size = size)

    def download(self, file_hash):
        self.ipfs.get(file_hash)
        for k, elem in enumerate(self.files):
            if elem.get('hash') == file_hash:
                file_name = self.files[k]['name']
                os.rename(os.path.join(self.DOWNLOAD_PATH,file_hash), os.path.join(self.DOWNLOAD_PATH,file_name))
                break
    def delete(self, file_hash):
        self.client.delete(hash = file_hash)
        self.update_files()
    def list_files(self):
        return self.files

    def update_files(self):
        self.files = self.client.list_files()

if __name__ == '__main__':
    api = Api()
    print(api.list_files())
    api.add('/home/ufo/vir.py')
