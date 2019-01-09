import requests
class request_1:
    def getrequests(self,url,data):
        return requests.get(url,data).json()
    def postrequests(self,url,data):
       return requests.post(url,data).json()

