import socket
import string
import random

#Funcion para quitar espacios y volver la palabra a minusculas
def cleanWord(word):
    return word.strip().lower()
#Revisa los resultados y asigna un puntaje
def totalScore(word):
    score = 0
    if word[0] in open('Data/mujeres').read():
        score += 10
    if word[1] in open('Data/hombres').read():
        score += 10
    if word[2] in open('Data/apellidos').read():
        score += 10
    if word[3] in open('Data/paises').read():
        score += 10
    if word[4] in open('Data/colores').read():
        score += 10
    return score
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
    #Nombre de mujer#
    sc1.send("Ingrese un nombre de mujer que comience con " + lttr + '\n')
    sc2.send("Ingrese un nombre de mujer que comience con " + lttr + '\n')

    rec1 = cleanWord(sc1.recv(1024))
    print(rec1)

    rec2 = cleanWord(sc2.recv(1024))
    print(rec2)

    tot1[0] = rec1
    tot2[0] = rec2
    
    #Nombre de hombre#
    sc1.send("Ingrese un nombre de hombre que comience con " + lttr + '\n')
    sc2.send("Ingrese un nombre de hombre que comience con " + lttr + '\n')

    rec1 = cleanWord(sc1.recv(1024))
    print(rec1)

    rec2 = cleanWord(sc2.recv(1024))
    print(rec2)

    tot1[1] = rec1
    tot2[1] = rec2

    #Apellido#
    sc1.send("Ingrese un apellido que comience con " + lttr + '\n')
    sc2.send("Ingrese un apellido que comience con " + lttr + '\n')

    rec1 = cleanWord(sc1.recv(1024))
    print(rec1)

    rec2 = cleanWord(sc2.recv(1024))
    print(rec2)

    tot1[2] = rec1
    tot2[2] = rec2

    #Pais#
    sc1.send("Ingrese un pais que comience con " + lttr + '\n')
    sc2.send("Ingrese un pais que comience con " + lttr + '\n')

    rec1 = cleanWord(sc1.recv(1024))
    print(rec1)

    rec2 = cleanWord(sc2.recv(1024))
    print(rec2)

    tot1[3] = rec1
    tot2[3] = rec2

    #Color#
    sc1.send("Ingrese un color que comience con " + lttr + '\n')
    sc2.send("Ingrese un color que comience con " + lttr + '\n')

    rec1 = cleanWord(sc1.recv(1024))
    print(rec1)

    rec2 = cleanWord(sc2.recv(1024))
    print(rec2)

    tot1[4] = rec1
    tot2[4] = rec2

    #Puntaje jugador 1
    print(totalScore(tot1))
    sc1.send(totalScore(tot1))

    #Puntaje jugador 2
    print(totalScore(tot2))
    sc1.send(totalScore(tot2))

    break
