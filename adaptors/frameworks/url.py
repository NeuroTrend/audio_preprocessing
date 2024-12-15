import os.path
import requests

class URLAdaptor:
    def __init__(self, url):
        self.url = url
        self.responseHead = None


    def localExists(self):
        return os.path.exists(self.url)
    
    def localIsDir(self):
        return os.path.isdir(self.url)
    
    def localIsFile(self):
        return os.path.isfile(self.url)
    
    def httpExists(self):
        if self.responseHead is not None:
            self.responseHead = requests.head(self.url)
        return self.responseHead.status_code == 200
    
    def httpIsDir(self):
        if self.responseHead is not None:
            self.responseHead = requests.head(self.url)
        return self.responseHead.headers['Content-Type'] == 'text/html'
    
    def httpIsFile(self):
        if self.responseHead is not None:
            self.responseHead = requests.head(self.url)
        return self.responseHead.headers['Content-Type'] != 'text/html'