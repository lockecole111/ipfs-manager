import ipfsapi

class IPFS:
    def __init__(self):
        try:
            with open ('../config.json') as f:
                self.config = json.loads(f.read())
        except FileNotFoundError:
            raise

        self.HOST = self.config['IPFS']['HOST']
        self.PORT = self.config['IPFS']['PORT']
        try:
            self.api = ipfsapi.connect(self.HOST, self.PORT)
        except Exception:
            raise

    def add(self, file_path):

        return self.api.add(file_path)
