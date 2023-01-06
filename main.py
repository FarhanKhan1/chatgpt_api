from pyChatGPT import ChatGPT
import time 
api = ChatGPT(auth_type='google', email='', password='')

resp = api.send_message("write a summarized essay on Allama Iqbal.")

print(resp['message'])
time.sleep(20)
