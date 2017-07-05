import socket

s = socket.socket()
s.connect(('127.0.0.1', 9999))
print("Conectado")
rec = s.recv(1024) 
print("La letra es " + rec + '\n')

while True:
    print(s.recv(1024) + '\n')
    msj = raw_input('>>>')
    s.send(msj)

    print(s.recv(1024) + '\n')
    msj = raw_input('>>>')
    s.send(msj)

    print(s.recv(1024) + '\n')
    msj = raw_input('>>>')
    s.send(msj)

    print(s.recv(1024) + '\n')
    msj = raw_input('>>>')
    s.send(msj)

    print(s.recv(1024) + '\n')
    msj = raw_input('>>>')
    s.send(msj)
    if msj == 'q':
        break
    