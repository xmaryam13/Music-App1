import socket 
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None 
BUFFER_SIZE = 4096
clients = {}


def acceptConnection():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        print(client, addr)
        
        


def set_up():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)
    
    print('\t\t\t\SERVER IS WAITING FOR INCOMING CONNECTION...')
    print('\n')
    
    acceptConnection()
    
setup_thread = Thread(target=set_up)
setup_thread.start()

    
        