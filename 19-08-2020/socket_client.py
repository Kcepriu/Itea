import socket
import time


HOST = '127.0.0.1'
PORT = 9103

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind((HOST, PORT))

try:
    while True:
        client_socket.send(b'Hello world')
        server_responce = client_socket.recv(1024)
        print(server_responce)
        time.sleep(2)
except KeyboardInterrupt:
    client_socket.close()


    # Метакласс
    # изменяеміе и не изменеяміе
    # декоратор
    # OPP полиморфизмб гаследование ...
    # filter map
    #  для чего служат * і **
    # что такоґе дескриптор get set
    # getattr setattr
    #rfrfz hf[ybwf пуе_фек  іуе_фек


