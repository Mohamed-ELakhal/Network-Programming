# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:54:52 2023

@author: moham
"""

import threading
import socket 

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
alias=input("choose alias >>> ")
client.connect(('127.0.0.1',59000))

def client_receieve():
    while True:
        try:
            message=client.recv(1024).decode('utf=8')
            if message=="alias?":
                client.send(alias.encode('utf=8'))
            else:
                print(message)
                
        except:
            print('Error!!')
            client.close()
            break
        
def client_send():
    while True:
        message=f'{alias} : {input("")}'
        client.send(message.encode('utf=8'))
        
receieve_thread=threading.Thread(target=client_receieve)
receieve_thread.start()
send_thread=threading.Thread(target=client_send)
send_thread.start()