import csv
import random
from itertools import count
def registrar_jugada(categoria, p1, p2):

    archivo = "jugadas.csv"
    existe = False
    try:
        with open(archivo, "r") as f:
            existe = True
    except FileNotFoundError:
        existe = False

    with open(archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        if not existe:
            escritor.writerow(["jugada", "j1", "j2"])
        escritor.writerow([categoria, p1, p2])

def jugadores_f():
    j1=[]
    j2=[]
    for i in range(5):
        j1.append(0)
        j2.append(0)
    return j1,j2

def dado():
    dados=[]
    for i in range(5):
        dados.append(0)
    print(dados)
    return dados
def cambiar_dados(dados):
    aux=0
    while aux<2:

        cambio=input("Desea cambiar dados responda si/no")
        if cambio=="si":
            aux+=1
            sting=input("ingrese dados a cambiar formato ejemplo: 0,1,2,3")#asume que el usario elige del 0 al 5
            dados_c=sting.split(",")
            for i in dados_c:
                dados[int(i)]= random.randint(1,6)
            print(f"los dados nuevo son{dados}")
        else:
            aux=3
            print(f"El jugador no cambia dados: {dados}")
    return

def tirada():
    dados= dado()

    for i in range(5):
        dados[i]=random.randint(1,6)
    print(f"Tu primer tiro es: {dados}")
    cambiar_dados(dados)
    print(f"Tus dados finales son: {dados}")
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
    lista=[]
    for i in dados:
        if i not in lista:
            lista.append(i)
    if len(lista)==2:
        if dados.count(lista[0])==3 or dados.count(lista[1])==3:#la funcion count returnea la cantidad de elementos en la lista
            return True
    else:
        return False
def poker(dados):
    aux=0
    for i in dados:
        if dados.count(i)==4:
            return True
    return False
def generala(dados):
    if dados.count(dados[0])==5:
        return True
    else:
        return False




def accion_valida(accion,jugador,dados):
    if accion=="E" and jugador[0]==0:# se supone que el usuario sabe que hizo y que no, en caso de seleccionar una opcion invalida no suma puntos
        print("Es valido")
        return True

    elif accion == "F" and jugador[1]==0 and Full(dados):
        print("Es valido")
        return True
    elif accion == "P" and jugador[2]==0 and poker(dados):
        print("Es valido")
        return True
    elif accion == "G" and jugador[3]==0 and generala(dados):
        print("Es valido")
        return True
    elif accion == "Num" and jugador[4]==0:
        print("Es valido")
        return True

    else:
        print("es invalido")
        return False

def sumar_dados(dados, elegidos):
    suma = 0
    for d in dados:
        if d == int(elegidos): # Convertir a int porque input da str
            suma += d
    return suma

def puntaje(jugador,dados,turnito):
    print(f"Tus puntajes actuales: {jugador}")

    accion = input(" Ingrese que desea registrar respete formato E o F o P o G o Num")
    if accion_valida(accion,jugador,dados):
        if accion=="E":#EFP
            jugador[0]=20
            if turnito==0:
                jugador[0]=25
            print(f"Puntaje actualizado: {jugador}")
        elif accion=="F":
            jugador[1]=30
            if turnito==0:
                jugador[0]=35
            print(f"Puntaje actualizado: {jugador}")
        elif accion =="P":
            jugador[2]=40
            if turnito==0:
                jugador[0]=45
            print(f"Puntaje actualizado: {jugador}")
        elif accion=="G":
            jugador[3]=50
            if turnito==0:
                jugador[0]=85
            print(f"Puntaje actualizado: {jugador}")
        elif accion=="Num":
            num=input("ingrese que dado desea sumar 1,2,3,4,5,6.")
            jugador[4]=sumar_dados(dados,num)
            print(f"Puntaje actualizado: {jugador}")

        else:
            accion= input("Elija que casilla ocupar con 0 : 0,1,2,3 o 4")
            jugador[int(accion)]=0
            print(f"Puntaje : {jugador}")




def turnos():
    j1,j2=jugadores_f()
    turnito1=0
    turnito2=0
    juegogeneral=0
    dadosj1=[]
    dadosj2=[]


    turnoj1=True
    turnoj2=True
    arranca=input("Quien arranca respetar formato: j1/j2 ")# que esto este en la funcion juego
    if arranca=="j1":
        turnoj1=False
    elif arranca=="j2":
        turnoj2=False
    while juegogeneral<=10:
        print(f"\n--- RONDA {juegogeneral} ---")
        juegogeneral+=1
        while not  turnoj1:
            print("\n>>> TURNO JUGADOR 1")
            dadosj1 = tirada()
            puntaje(j1,dadosj1,turnito1)
            if j1[3]== 85 and turnito1==0:
                print("Finalizo el juego. Generala real del jugador 1.")
                break
            turnoj2=False
        while not  turnoj2:
            print("\n>>> TURNO JUGADOR 2")
            dadosj2=tirada()
            puntaje(j2,dadosj2,turnito2)
            if j1[3]== 85 and turnito2==0:
                print("Finalizo el juego. Generala real del jugador 3.")
                break
            turnoj1=False

turnos()