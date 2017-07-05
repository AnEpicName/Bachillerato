import socket
import pickle

answ = ['','','','','']

s = socket.socket()
s.connect(('127.0.0.1', 9999))
print("Conectado")
rec = s.recv(1024) 
print("La letra es: " + rec + '\n')

while True:
    print("Ingrese un nombre de mujer que comience con " + rec)
    answ[0] = raw_input('>>>')

    print("Ingrese un nombre de hombre que comience con " + rec)
    answ[1] = raw_input('>>>')

    print("Ingrese un apellido que comience con " + rec)
    answ[2] = raw_input('>>>')

    print("Ingrese un pais que comience con " + rec)
    answ[3] = raw_input('>>>')

    print("Ingrese un color que comience con " + rec)
    answ[4] = raw_input('>>>')

    answ = pickle.dumps(answ)
    s.send(answ)
    print("Esperando al otro jugador...\n")

    print(s.recv(1024))
    break