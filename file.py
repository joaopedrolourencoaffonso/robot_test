import socket
from threading import *
from _thread import *
import random;
import time

def enviar(connection, i):
    ip = "192.168.0.";
    global t;

    while True:
        i = 1;
        tempo = random.randint(15, 30);
        t = 0;
        while t < tempo:
            print(t);
            time.sleep(1);
            t = t + 1;
           
        while i < 255:
            serverAddressPort_ip = ip + str(i);
            i = i + 1;

            msgFromClient       = "Hello UDP Server";
            bytesToSend         = str.encode(msgFromClient);
            serverAddressPort   = (serverAddressPort_ip, 22000);
            bufferSize          = 1024;

            # Create a UDP socket at client side
            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM);

            # Send to server using created UDP socket
            UDPClientSocket.sendto(bytesToSend, serverAddressPort);
            print(i);

def receber(connection, i):
    global t;
    localIP     = "192.168.0.114";
    localPort   = 21000;
    bufferSize  = 1024;
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM);
    UDPServerSocket.bind((localIP, localPort));
    print("Up and listening");
    
    while True:
        msgFromServer = UDPServerSocket.recvfrom(bufferSize);
        msg = "Message {}".format(msgFromServer[0]);
        msg1 = "Message {}".format(msgFromServer[1]);
        t = 0;
        
        print(msg);
        print(msg1)

###########################    
tempo = 30;

Client = "temp";
ThreadCount = 1;

start_new_thread(enviar, (Client, ThreadCount));
start_new_thread(receber, (Client, ThreadCount));
