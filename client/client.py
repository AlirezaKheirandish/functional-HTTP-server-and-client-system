#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 02:52:40 2021

@author: alirezakheirandish
"""

import socket 
import time
import os

direction = '/Users/alirezakheirandish/Downloads/PROJ/CLIENT'

Port = 5056

Format = "utf-8"
T = 0.001

# Server = socket.gethostbyname(socket.gethostname())
Server = '127.0.0.1'
Addr = (Server, Port)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(Addr)
# time.sleep(T)

def telnet (msg):
    time.sleep(T)

    msg = ' '.join(msg.split())
    if msg == "number of connected clients" or msg == "file type stats" or msg == "request stats" or msg == "response stats" or msg == "disconnect" :
        time.sleep(T)

        if msg != "disconnect":
            time.sleep(T)

            
            cl = client.recv(4096)
                    
            print (cl.decode('utf-8'))
            return 1
        else:
            time.sleep(T)
            return 1
    time.sleep(T)

    return 0

def extended (msg):
    if len(msg) ==  1 :
        return '0'*7+msg
    if len(msg) ==  2:
        return '0'*6+msg
    if len(msg) ==  3:
        return '0'*5+msg
    if len(msg) ==  4:
        return '0'*4+msg
    if len(msg) ==  5:
        return '0'*3+msg
    if len(msg) ==  6:
        return '0'*2+msg
    if len(msg) ==  7:
        return '0'+msg
    return msg
    
    
    
def post (msg):
    time.sleep(T)

    chk = msg.split('\n')
    ch = chk[0].split('/')
    c = ch[0].split()[0]
    dirr = direction
    if len(ch) < 3 :
        time.sleep(T)
        return 0
    
    if ch[-1].split()[0] != '1.1':
        time.sleep(T)
        if ch[-1].split()[0] != '1.0':
            time.sleep(T)
            return 0
    if ch[-2].split()[-1] != 'HTTP':
        time.sleep(T)
        return 0
    L = len(chk)
    for i in range(1,L):
        time.sleep(T)
        if len(chk[i].split()) != 0:
            ch = chk[i].split(':')
            if len(ch) < 2 :
                time.sleep(T)
                return 0
            if len(ch[1]) == 0 or len(ch[0]) == 0 :
                time.sleep(T)
                return 0
    if c == 'POST':
        time.sleep(T)

        if not os.path.exists(dirr + chk[0].split()[1]):
            time.sleep(T)

            print ('ADDRESS UNREACHABLE')
        return os.path.getsize(dirr + chk[0].split()[1])
    time.sleep(T)

    return 0


def send(msg):
    
    time.sleep(T)
    message = msg.encode(Format)
    client.send(message)
    time.sleep(0.01)
    if telnet(msg):
        return
    
    if post(msg):
        time.sleep(T)
        client.send(extended(str(post(msg))).encode('utf-8'))
        if post(msg) >= 51 :
            chk = msg.split('\n')
            f = open(direction+chk[0].split()[1],'rb')
            l = f.read(51)
            time.sleep(T)
            client.send(l)
            f.close()
        
        
    time.sleep(T)
    cl = client.recv(4096)
    time.sleep(0.01)
    num = int(cl[0:3])
    cli = cl[3:num+2].decode(Format)
    # print (cli)
    if cli.find('Allow: ') + 1 :
        time.sleep(T)

        fo = cli[cli.find('Content-Type')+len('Content-Type: '):cli.find('Allow: ')-2].split('/')[1]
    else :
        time.sleep(T)
        fo = cli[cli.find('Content-Type')+len('Content-Type: '):cli.find('Date: ')-2].split('/')[1]
        
    name = time.ctime().split()[-2]
    name = name + '.'+fo
    time.sleep(T)
    f = open (direction+ '/'  + name,'ab')
    f.write(cl[num+3:])

    print (cli)

    while 1:
        time.sleep(T)

        if cl[num+3:] == b'<html><body><h1>POST!</h1></body></html>' or cl[num+3:] == b'<html><body><h1>FORBIDDEN!</h1></body></html>':
            time.sleep(T)
            f.close()
            break
        time.sleep(T)


        if len(cl) == 0:
            time.sleep(T)
            break
        
        if len(cl) < 4096:
            time.sleep(T)
            f.write(cl)
            break
        
        cl = client.recv(4096)
        f.write(cl)
    f.close()
    if post(msg):
        time.sleep(T)
        chk = msg.split('\n')
        f = open(direction + chk[0].split()[1],'rb')
        time.sleep(T)
        f.seek(51)
        l = f.read()
        time.sleep(T)
        f.close()
        time.sleep(T)
        client.send(l)
        time.sleep(T)

        
    time.sleep(T)

    print (f'$ \n{name}\n$ \n')
    return

    
    
# send("HELLO")
# send("disconnect")
# time.sleep(1000*T)
# send(" file type stats")
# time.sleep(T)
# send("number of connected clients")
# time.sleep(T)
# send("request stats ")
# send("response stats")
send('''POST /forb.html HTTP/1.1
# #         Host: developer.mozilla.org
       # Accept-Language: fr''')

# time.sleep(T)
# send('''GET /aks.png hTTP/1.1
#       Host: developer.mozilla.org
#       Accept-Language: fr''')
# time.sleep(1000*T)
send('''DELETE / HTTP/1.1
#       Host: developer.mozilla.org
#       Accept-Language: fr''')
# time.sleep(1000*T)
# time.sleep(T)
# send('''GET /aks11.jpeg HTTP/1.1
#       Host: developer.mozilla.org
#       Accept-Language: fr''')
# time.sleep(T)
     

# time.sleep(T)
# time.sleep(T)

# send('''GET /cvxopt.html HTTP/1.1
        # Host: developer.mozilla.org
       # Accept-Language: fr''')
     
     
     
     
     
     
     
     