import json
from client import Client
from ipfs import IPFS

class Api:

    def __init__(self):
        self.ipfs = IPFS()
        self.client = Client()
    def add(self, file_path):
        add_info = self.ipfs.add(file_path)
        hash = add_info['Hash']
        name = add_info['Name']
        size = add_info['Size']
        self.client.add(name = name, hash = hash, size = size)

    def download(self, file_hash):
        self.ipfs.get(file_hash)
        
    def delete(self, file_hash):
        self.client.delete(hash = file_hash)

    def list_files(self):
        return self.client.list_files()

if __name__ == '__main__':
    api = Api()
    print(api.list_files())

