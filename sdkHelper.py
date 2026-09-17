import requests
class sdkHelper:
    url = "https://tapi.bale.ai/bot"
    def printName(self,name = "stranger"):
        print(f"hello dear {name}")

    def w3scholls(self):
        x = requests.get("https://www.w3schools.com/python/demopage.php")
        print(x.text)
    def sendMessage(self,token,chat_id,text = ""):
        x = requests.get(f"{self.url}{token}/sendMessage",json = {'chat_id' : chat_id ,'text' : text})
        print(x)
    def getUpdates(self, token):
        response = requests.get(f"{self.url}{token}/getUpdates")
        return response.json()