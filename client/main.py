import socket


HOST = '127.0.0.1'
PORT = 5000

while True:
    print("Digite o número do CPF [0 para sair]")
    cpf = input()

    if cpf == '0':
        quit()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
        tcp.connect((HOST, PORT))
        tcp.send(cpf.encode())
        data = tcp.recv(1024).decode()

    print(f'O CPF {cpf} é {data}')
