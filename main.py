from pyChatGPT import ChatGPT
import config
import time 

email = config.email
password = config.password

api = ChatGPT(auth_type='google', email=email, password=password)

while True:
    
    prompt = input("Ask chatGPT: ")
    resp = api.send_message(prompt)

    print(resp['message'])
    #time.sleep(20)
