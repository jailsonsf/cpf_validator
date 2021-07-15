import socket
from cpf_validator import *

HOST = '127.0.0.1'
PORT = 5000

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
        tcp.bind((HOST, PORT))
        tcp.listen(1)

        connection, client = tcp.accept()
        print(f'Conectado com {connection}')

        with connection:
            while True:
                cpf = connection.recv(1024)
                if not cpf:
                    break

                else:
                    cpf = cpf.decode()
                    print(cpf)

                    if (cpfValidate(cpf)):
                        res = 'Válido'
                        connection.sendall(res.encode())

                    elif (cpfValidate(cpf) == False):
                        res = 'Inválido'
                        connection.sendall(res.encode())
