import ipfsapi
import json

class IPFS:
    def __init__(self):
        try:
            with open ('../config.json') as f:
                self.config = json.loads(f.read())
        except FileNotFoundError:
            raise
        self.DOWNLOAD_PATH = self.config['CLIENT']['DOWNLOAD_PATH']
        self.HOST = self.config['IPFS']['HOST']
        self.PORT = self.config['IPFS']['PORT']
        try:
            self.api = ipfsapi.connect(self.HOST, self.PORT)
        except Exception:
            raise

    def add(self, file_path):

        return self.api.add(file_path)
    def get(self, file_hash, file_path):
        return self.api.get(file_hash, filepath = self.DOWNLOAD_PATH)
