import socket


def start():
    server.listen()
    print("Server is listening on {a}".format(a=address))

    while True:
        conn, client_address = server.accept()

        data = conn.recv(buffer_size).decode(format_)
        if not data:
            break

        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(format_))
        conn.send("<!DOCTYPE html><html><body><h1>WEB BROWSER</h1><p>HI! Sounds awesome</p></body></html>".encode(format_))

# Server = socket.gethostbyname(socket.gethostname())
Server = '127.0.0.1'
address = (Server, 9001)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
format_ = "utf-8"
buffer_size = 4096





start()
