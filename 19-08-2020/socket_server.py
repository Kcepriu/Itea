import socket


HOST = '127.0.0.1'
PORT = 9103

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_obj.bind((HOST, PORT))
socket_obj.listen(10)

while True:

    conn, addr = socket_obj.accept()
    while True:
        date = conn.recv(1024)
        if not date:
            break
        conn.send(date[::-1])
        print(date)

    conn.close()
