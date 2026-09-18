import requests
class sdkHelper:
    url = "https://tapi.bale.ai/bot"
    entryKeyboard = {
        "keyboard" : [
            [{"text":"شروع"}]
        ],"resize_keyboard":True
    }
    def getMe(self,token):
        if len(token) == 0:
            return "token is missing"
        # validate token
        response = requests.post(f"{self.url}{token}/getMe").json()
        if not response['ok']:
            return "invalid token"
        return(response['result'])

    def sendMessage(self,token,chat_id,text,reply_markup = None):
        if not token:
            return "token is missing"
        if not chat_id:
            return "chat id is missing"
        if not text:
            return "text id is missing"
        response = requests.get(f"{self.url}{token}/sendMessage",json={"chat_id": chat_id,"text": text,"reply_markup": reply_markup}).json()
        return response
        
    def getUpdates(self, token):
        if len(token) < 1:
            return "token is missing"
        response = requests.get(f"{self.url}{token}/getUpdates").json()
        updates_id = [item['update_id'] for item in response['result']]
        message = [item['message'] for item in response['result']]
        messageFrom = [item['from'] for item in message]
        for item in message:
             if 'text' in item:
                 if item['text'] == '/start':
                     if item['from']['id']:
                         print(
                             self.sendMessage(token,item['from']['id'],"سلام 👋",self.entryKeyboard))

            