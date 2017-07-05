import socket
import string
import random
import pickle
from unidecode import unidecode

#Funcion para quitar espacios y volver la palabra a minusculas
def cleanWord(word):
    word = word.strip().upper()
    clnwrd = unidecode(word)
    clnwrd.encode("ascii")
    return clnwrd
#Revisa los resultados y asigna un puntaje
def totalScore(word):
    score = 0
    if cleanWord(word[0]) in open('Data/mujeres').read().upper():
        score += 10
    if cleanWord(word[1]) in open('Data/hombres').read().upper():
        score += 10
    if cleanWord(word[2]) in open('Data/apellidos').read().upper():
        score += 10
    if cleanWord(word[3]) in open('Data/paises').read().upper():
        score += 10
    if cleanWord(word[4]) in open('Data/colores').read().upper():
        score += 10
    return score
#Determina al ganador
def winner(p1, p2):
    if p1 > p2:
        return 1
    elif p1 < p2:
        return 2
    elif p1 == p2:
        return 0
#Elige una letra al azar para comenzar el juego
lttr = random.choice(string.ascii_uppercase)
tot1 = ['','','','','']
tot2 = ['','','','','']

print 'Corriendo...'
s = socket.socket()
s.bind(('', 9999))
s.listen(2)

sc1, addr = s.accept()
print('Se ha conectado el primer jugador.')
sc2, addr = s.accept()
print('Se ha conectado el segundo jugador.')

print('La letra es ' + lttr + '\n')
sc1.send(lttr)
sc2.send(lttr)

while True:
    print("start")
    #Puntaje jugador 1
    res1 = pickle.loads(sc1.recv(1024))
    print(totalScore(res1))
    tot1 = totalScore(res1)
    #sc1.send(str(tot1))

    #Puntaje jugador 2
    res2 = pickle.loads(sc2.recv(1024))
    print(totalScore(res2))
    tot2 = totalScore(res2)

    if winner(tot1, tot2) == 1:
        sc1.send("Has ganado. Obtuviste " + str(tot1) + " puntos.")
        sc2.send("Has pedido. Obtuviste " + str(tot2) + " puntos.")
    elif winner(tot1, tot2) == 2:
        sc1.send("Has pedido. Obtuviste " + str(tot1) + " puntos.")
        sc2.send("Has ganado. Obtuviste " + str(tot2) + " puntos.")
    elif winner(tot1, tot2) == 0:
        sc1.send("Empate. Obtuviste " + str(tot1) + " puntos.")
        sc2.send("Empate. Obtuviste " + str(tot2) + " puntos.")
    break
