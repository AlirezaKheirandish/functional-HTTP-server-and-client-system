#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
#import json
#jsonFile = open("/Users/alirezakheirandish/Downloads/PROJ/SERVER/telnet.json", "w")
#part4 = {'NUM':0,'JPG':0,'TEXT':0,'PNG':0,'GET':0,'PUT':0,'POST':0,'DELETE':0,'HEAD':0,'Improper':0,'A_400':0,'A_501':0,'A_405':0,'A_200':0,'A_301':0,'A_403':0}
#jsonString = json.dumps(part4)
#jsonFile.write(jsonString)
#jsonFile.close()
# =============================================================================


"""
Created on Sun Jul 11 18:18:28 2021

@author: alirezakheirandish
"""

import socket
import threading
import time
import os
import json



part3 = {
    'ADDR' : '192.168.0.1:500',
    'Rtype' : 'GET',
    'TYPE' : 'OK',
    'time' : time.ctime() 
    }

direction = "/Users/alirezakheirandish/Downloads/PROJ/SERVER"
T = 0.0001
disconnect = 0 

time.sleep(T)
fileObject = open(direction + "/telnet.json", "r")
jsonContent = fileObject.read()
part4 = json.loads(jsonContent)
time.sleep(T)


Port = 5057


# Server = socket.gethostbyname(socket.gethostname())
Server = '127.0.0.1'
Addr = (Server, Port)
Format = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(Addr)
time.sleep(T)

def BAD_REQUEST (msg):
    time.sleep(T)
    s1 = 'HTTP/1.0 400 Bad Request\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(len('<html><body><h1>BADREQUEST!</h1></body></html>'))+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>BADREQUEST!</h1></body></html>\r\n'
    output = s1+s2+s3+s4+s5+s6
    le = len(s1+s2+s3+s4+s5)
    chk = msg.split('\n')
    ch = chk[0].split('/')
    sit = '0'
    time.sleep(T)
    if len(ch) < 3 :
        time.sleep(T)
        sit = '1'
        part4.update(Improper = part4.pop('Improper') + 1)
        return [output,le,sit]
    
    if ch[-1].split()[0] != '1.1':
        time.sleep(T)
        if ch[-1].split()[0] != '1.0':
            time.sleep(T)
            sit = '1'
            part4.update(Improper = part4.pop('Improper') + 1)
            return [output,le,sit]
    if ch[-2].split()[-1] != 'HTTP':
        time.sleep(T)
        sit = '1'
        part4.update(Improper = part4.pop('Improper') + 1)
        return [output,le,sit]
    c = ch[0].split()[0]
    L = len(chk)
    part3.update(Rtype = c)
    if c == 'POST':
        time.sleep(T)
        part4.update(POST = part4.pop('POST') + 1)
    elif c == 'GET':
        time.sleep(T)
        part4.update(GET = part4.pop('GET') + 1)
    elif c == 'DELETE':
        time.sleep(T)
        part4.update(DELETE = part4.pop('DELETE') + 1)
    elif c == 'HEAD':
        time.sleep(T)
        part4.update(HEAD = part4.pop('HEAD') + 1)
    elif c == 'PUT':
        time.sleep(T)
        part4.update(PUT = part4.pop('PUT') + 1)
    else :
        time.sleep(T)
        part4.update(Improper = part4.pop('Improper') + 1)
        
    for i in range(1,L):
        time.sleep(T)
        if len(chk[i].split()) != 0:
            ch = chk[i].split(':')
            if len(ch) < 2 :
                time.sleep(T)
                sit = '1'
                part4.update(Improper = part4.pop('Improper') + 1)
                return [output,le,sit]
            if len(ch[1]) == 0 or len(ch[0]) == 0 :
                time.sleep(T)
                sit = '1'
                part4.update(Improper = part4.pop('Improper') + 1)
                return [output,le,sit]
    
    time.sleep(T)
    return [output,le,sit]
    

def NOT_IMPLEMENTED(msg):
    time.sleep(T)
    s1 = 'HTTP/1.0 501 Not Implemented\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(len('<html><body><h1>NOTIMPLEMENTED!</h1></body></html>'))+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>NOTIMPLEMENTED!</h1></body></html>'
    output = s1+s2+s3+s4+s5+s6
    le = len(s1+s2+s3+s4+s5)
    chk = msg.split('\n')
    ch = chk[0].split('/')
    sit = '1'
    if len(ch[0].split()) != 1:
        time.sleep(T)
        sit = '1'
        return [output,le,sit]
    c = ch[0].split()[0]
    part3.update(Rtype = c)
    if c == 'PUT' or c == 'POST' or c == 'DELETE' or c == 'HEAD' or c == 'GET':
        time.sleep(T)
        sit = '0'
    time.sleep(T)
    return [output,le,sit]
    
def NOT_ALLOWED(msg):
    time.sleep(T)
    s1 = 'HTTP/1.0 405 Method Not Allowed\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(len('<html><body><h1>NOTALLOWED!</h1></body></html>'))+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    S4 = 'Allow: GET\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>NOTALLOWED!</h1></body></html>'
    output = s1+s2+s3+s4+S4+s5+s6
    le = len(s1+s2+s3+s4+S4+s5)
    chk = msg.split('\n')
    ch = chk[0].split('/')
    c = ch[0].split()[0]
    sit = '1'
    if c == 'POST' or c == 'GET':
        time.sleep(T)
        sit = '0'
    time.sleep(T)
    return [output,le,sit]

def GET_ADDR(msg):
    time.sleep(T)
    s1 = 'HTTP/1.0 301 Moved Permanently\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(len('<html><body><h1>MOVEDPERMANENTLY!</h1></body></html>'))+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>MOVEDPERMANENTLY!</h1></body></html>'
    output = s1+s2+s3+s4+s5+s6
    le = len(s1+s2+s3+s4+s5)
    chk = msg.split('\n')
    ch = chk[0].split('/')
    c = ch[0].split()[0]
    part3.update(Rtype = c)
    sit = '0'
    dirr = direction
    if c == 'GET':
        time.sleep(T)
        sit = '1'
        if os.path.exists(dirr + chk[0].split()[1]):
            time.sleep(T)
            sit = '0'
    time.sleep(T)
    return [output,le,sit]
    


def GET_OK(msg,conn,addr):
    global disconnect
    time.sleep(T)
    Format = 'utf-8'
    Output,le,Sit = BAD_REQUEST (msg)
    if Sit == '1':
        time.sleep(T)
        part3.update(TYPE = '400 Bad Request')
        part4.update(A_400 = part4.pop('A_400') + 1)
        conn.sendto(str(le).encode(Format)+Output.encode(Format),addr)
        # conn.close()
        # disconnect = 1
        return [Output,le,Sit]
    
    Output,le,Sit = NOT_IMPLEMENTED(msg)
    if Sit == '1':
        time.sleep(T)
        part3.update(TYPE = '501 Not Implemented')
        part4.update(A_501 = part4.pop('A_501') + 1)
        conn.sendto(str(le).encode(Format)+Output.encode(Format),addr)
        # conn.close()
        # disconnect = 1
        return [Output,le,Sit]
    
    Output,le,Sit = NOT_ALLOWED(msg)
    if Sit == '1':
        time.sleep(T)
        part3.update(TYPE = '405 Method Not Allowed')
        part4.update(A_405 = part4.pop('A_405') + 1)
        conn.sendto(str(le).encode(Format)+Output.encode(Format),addr)
        # disconnect = 1
        return [Output,le,Sit]
    
    Output,le,Sit = GET_ADDR(msg)
    if Sit == '1':
        time.sleep(T)
        part3.update(TYPE = '301 Moved Permanently')
        part4.update(A_301 = part4.pop('A_301') + 1)
        conn.sendto(str(le).encode(Format)+Output.encode(Format),addr)
        # disconnect = 1
        return [Output,le,Sit]
    
    time.sleep(T)
    chk = msg.split('\n')
    ch = chk[0].split('/')
    c = ch[0].split()[0]
    dirr = direction
    sit = '0'
    if c != 'GET':
        time.sleep(T)
        disconnect = 1
        return ["OOOPS!!",1,sit]
    
    s1 = 'HTTP/1.0 200 OK\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(os.path.getsize(dirr + chk[0].split()[1]))+'\r\n'
    t = chk[0].split()[1].split('.')[1]
    if t == 'txt':
        time.sleep(T)
        t = 'text/txt'
        part4.update(TEXT = part4.pop('TEXT') + 1)
    elif t == 'jpeg':
        time.sleep(T)
        t = 'image/jpeg'
        part4.update(JPG = part4.pop('JPG') + 1)
    elif t == 'png':
        time.sleep(T)
        t = 'image/png'
        part4.update(PNG = part4.pop('PNG') + 1)
    elif t == 'html':
        time.sleep(T)
        t = 'text/html'
        part4.update(TEXT = part4.pop('TEXT') + 1)
    else :
        time.sleep(T)
        t = 'ERROR'
    time.sleep(T)        
    s4 = 'Content-Type: '+ t + '\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    output = s1+s2+s3+s4+s5
    le = len(output)
    time.sleep(T)
    
    f = open(dirr + chk[0].split()[1],'rb')
    
    l = f.read(3000)
    output = output.encode('utf-8') + l
    conn.sendto(str(le).encode(Format)+output,addr)
    tool = os.path.getsize(dirr + chk[0].split()[1])
    time.sleep(T)
    if tool > 3000:
        time.sleep(T)
        i = 1
        
        while tool >3000*(i+1):
            time.sleep(T)

            f.seek(3000*i)
            l = f.read(3000)
            conn.sendto(l,addr)
            i = i + 1
        f.seek(3000*i)
        l = f.read()
        conn.sendto(l,addr)
        time.sleep(T)

        time.sleep(T)
        part3.update(TYPE = '200 OK')
        part4.update(A_200 = part4.pop('A_200') + 1)
        time.sleep(T)
        # disconnect = 1

        return [output,le,'2']
        
    time.sleep(T)
    f.close()
    part3.update(TYPE = '200 OK')
    part4.update(A_200 = part4.pop('A_200') + 1)
    disconnect = 1
    return [output,le,'2']
    

def POST_FORBIDDEN(msg,conn):
    time.sleep(T)
    chk = msg.split('\n')
    s1 = 'HTTP/1.0 403 Forbidden\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(len('<html><body><h1>THISISFORBIDDEN!</h1></body></html>'))+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>FORBIDDEN!</h1></body></html>'
    Output = s1+s2+s3+s4+s5+s6
    le = len(s1+s2+s3+s4+s5)
    Sit = 0
    f = open (direction + '/' +chk[0].split()[1].split('/')[-1],'wb')
    msg = conn.recv(51)
    f.write(msg)
    if len(msg ) < 51 :
        time.sleep(T)
        print ("ERRRRRRROOOOOOORRRRR")
    f.close()
    f = open (direction + '/'+chk[0].split()[1].split('/')[-1],'rb')
    l = f.read(51)
    if l == b'<html><body><h1>THISISFORBIDDEN!</h1></body></html>':
        time.sleep(T)
        Sit = 1
        part3.update(TYPE = '403 Forbidden')
        part4.update(A_403 = part4.pop('A_403') + 1)
    f.close()
    time.sleep(T)
    return [str(le)+Output,Sit]
    

def POST_OK(msg,conn,addr):
    time.sleep(T)
    part3.update(Rtype = 'POST')
    chk = msg.split('\n')
    global disconnect
    LE = int (conn.recv(8).decode('utf-8'))
    time.sleep(T)
    s1 = 'HTTP/1.0 200 OK\r\n'
    s2 = 'Connection: close\r\n'
    s3 = 'Content-Length: '+str(LE)+'\r\n'
    s4 = 'Content-Type: text/html\r\n'
    s5 = 'Date: '+time.ctime()+'\r\n\r\n'
    s6 = '<html><body><h1>POST!</h1></body></html>'
    output = s1+s2+s3+s4+s5+s6
    le = len(s1+s2+s3+s4+s5)
    output = str(le) + output
    Sit = 0
    Output,Sit = POST_FORBIDDEN(msg,conn)
    if Sit == 0 :
        time.sleep(T)
        conn.sendto(output.encode('utf-8'),addr)
    else:
        time.sleep(T)
        disconnect = 1
        conn.sendto(Output.encode('utf-8'),addr)
        return
    
    time.sleep(T)
    f = open (direction + '/'+chk[0].split()[1].split('/')[-1],'ab')
    time.sleep(T)
    L = LE - 51
    time.sleep(T)
    time.sleep(T)
    L = 0
    msg = conn.recv(LE)
    f.write(msg)
    L = L + len(msg)
    while L != LE - 51:
        msg = conn.recv(L)
        if len(msg) == 0:
            break
        time.sleep(T)
        f.write(msg)
        L = L + len(msg)
    f.close()
    part3.update(TYPE = '200 OK')
    part4.update(A_200 = part4.pop('A_200') + 1)
    time.sleep(T)
    return
    
def telnet(msg,conn,addr):
    time.sleep(T)
    msg = ' '.join(msg.split())

    if msg == "number of connected clients":
        time.sleep(T)
        s1 = 'number of connected clients : ' + str (part4.get("NUM")) + '\r\n'
        conn.sendto(s1.encode('utf-8'),addr)
        return 0
    elif msg == "file type stats":
        time.sleep(T)
        s1 = "image/jpeg: "+str(part4.get("JPG"))+"\r\n"
        s2 = "text/txt: "+str(part4.get("TEXT"))+"\r\n"
        s3 = "image/png: "+str(part4.get("PNG"))+"\r\n"
        output = s1+s2+s3
        conn.sendto(output.encode('utf-8'),addr)
        return 0
    elif msg == "request stats":
        time.sleep(T)
        s1 = "GET: "+str(part4.get("GET"))+"\r\n"
        s2 = "PUT: "+str(part4.get("PUT"))+"\r\n"
        s3 = "POST: "+str(part4.get("POST"))+"\r\n"
        s4 = "DELETE: "+str(part4.get("DELETE"))+"\r\n"
        s5 = "HEAD: "+str(part4.get("HEAD"))+"\r\n"
        s6 = "Improper: "+str(part4.get("Improper"))+"\r\n"
        output = s1+s2+s3+s4+s5+s6
        conn.sendto(output.encode('utf-8'),addr)
        return 0
    elif msg == "response stats":
        time.sleep(T)
        s1 = "400: "+str(part4.get("A_400")) +"\r\n"
        s2 = "501: "+str(part4.get("A_501")) +"\r\n"
        s3 = "405: "+str(part4.get("A_405")) +"\r\n"
        s4 = "200: "+str(part4.get("A_200")) +"\r\n"
        s5 = "301: "+str(part4.get("A_301")) +"\r\n"
        s6 = "403: "+str(part4.get("A_403")) +"\r\n"
        output = s1+s2+s3+s4+s5+s6
        conn.sendto(output.encode('utf-8'),addr)
        return 0
    elif msg == "disconnect":
        time.sleep(T)
        global server
        global disconnect
        server.shutdown(socket.SHUT_RDWR)
        disconnect = 1
        conn.close()
        server.close()
        # if socket.error():
        #     thread.join()
        return 0
    else:
        return 1


def handle_client (conn, addr):
    print (f"[New connection]: {addr}: {Port} connected!")
    while 1 :
        time.sleep(T)
    
        msg = conn.recv(4096).decode(Format)
        if telnet(msg,conn,addr):
            time.sleep(T)
            
            print (msg)
            print (f"{addr}: \n {msg} \n")
            output,le,sit = GET_OK(msg,conn,addr)
            if sit == '0':
                time.sleep(T)
                POST_OK(msg,conn,addr)
            
        time.sleep(T)
        jsonString = json.dumps(part3)
        jsonFile = open(direction + "/data.json", "a")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        jsonFile = open(direction + "/telnet.json", "w")
        jsonString = json.dumps(part4)
        jsonFile.write(jsonString)
        jsonFile.close()
        time.sleep(T)
        time.sleep(T)
        # return 1
    return 1

    
    

def start():
    # while 1:
    server.listen()
    time.sleep(T)
    print (f"Server is listening on {Server}")
    # while not disconnect :
    while 1:
        time.sleep(T)
        conn, addr = server.accept()
        time.sleep(T)
        part3.update(ADDR = str(addr))
        time.sleep(T)
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        time.sleep(T)
        thread.start()
        print(f"Active Connections: {threading.activeCount()-1}") 
        part4.update(NUM = threading.activeCount()-1)
        if socket.error():
            thread.join()
            # break
        
time.sleep(T)
print ("Server is Starting")
start()
time.sleep(T)


