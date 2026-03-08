import csv
import random


def jugadores_f():
    j1=[]
    j2=[]
    for i in range(5):
        j1.append(0)
        j2.append(0)
def dado():
    dados=[]
    for i in range(5):
        dados.append(0)
    return dados
def cambiar_dados(dados):
    aux=0
    while aux<2:

        cambio=input("Desea cambiar dados responda si/no")
        if cambio=="si":
            aux+=1
            sting=input("ingrese dados a cambiar formato ejemplo: 0,1,2,3")#asume que el usario elige del 0 al 5
            dados_c=sting.split(",")
            for i in range(dados_c):
                dados[int(i)]= random.randint(1,6)
        else:
            aux=3
            print("El jugador no cambia dados")
    return

def tirada():
    dados= dado()

    for i in range(5):
        dados[i]=random.randint(1,6)
    cambiar_dados(dados)
    return dados
def escalera(dados):
    ordenados=sorted(dados)# la funcion sorted es un bublesort de menor a mayor
    esc=[1,2,3,4,5,]
    esc1=[2,3,4,5,6]
    if ordenados== esc or ordenados== esc1:
        return True
    else:
        return False
def Full(dados):


def accion_valida(accion,jugador,dados):
    if accion=="E" and jugador[0]==0:# se supone que el usuario sabe que hizo y que no, en caso de seleccionar una opcion invalida no suma puntos
        print("Es valido")
        return True

    elif accion == "F" and jugador[1]==0 :
        print("Es valido")
        return True
    elif accion == "P" and jugador[2]==0:
        print("Es valido")
        return True
    elif accion == "G" and jugador[3]==0:
        print("Es valido")
        return True
    elif accion == "Num" and jugador[4]==0:
        print("Es valido")
        return True

    else:
        print("es invalido")
        return False
def sumar_dados(dados):
    suma=0
    for i in dados:
        suma+=int(dados[i])
    return suma

def puntaje(jugador,dados):

    accion = input(" Ingrese que desea registrar respete formato E o F o P o G o Num")
    if accion_valida(accion,jugador,dados):
        if accion=="E":
            jugador[0]=20
        elif accion=="F":
            jugador[1]==30
        elif accion =="P":
            jugador[2]==40
        elif accion=="G":
            jugador[3]==50
        elif accion=="Num":
            jugador[4]==sumar_dados(dados)
        else:
            accion= input("Eliga que casilla ocupar con 0 : 0,1,2,3 o 4")
            jugador[int(accion)]=0















def turnos():
    j2=[]
    j1=[]
    dadosj1=[]
    dadosj2=[]
    jugadores_f()

    turnoj1=True
    turnoj2=True
    arranca=input("Quien arranca respetar formato: j1/j2 ")
    if arranca=="j1":
        turnoj1=False
    elif arranca=="j2":
        turnoj2=False
    aux=0
    while not  turnoj1:
        dadosj1 = tirada()    #queda asignar puntaje
        puntaje(j1,dadosj1)

