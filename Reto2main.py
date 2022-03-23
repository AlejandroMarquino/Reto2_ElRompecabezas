import random
from tempfile import tempdir
import numpy as np # numpy me ayuda al tratamiento del número en matriz y detecta y ayuda al script (la condición de búsqueda en linea 43)

# funciones

def showPuzzle(puzzle):
    
    i=0
    separacion=''
    while i<(len(puzzle)):
        i+=1
        separacion=separacion+'+----'
    separacion=separacion+'|'
    
    print(separacion)
        
    for x in range (len(puzzle)):
        for y in range(len(puzzle[x])):
            if puzzle[x][y] == np.max(puzzle):
                print('|' , end='    ')
            else:
                 print('|' + '{:02d}' .format(puzzle[x][y]), end='  ')

        print('\n'+separacion)

def rowSolver(puzzle,n,m): #Empiezo a hacer el puzzle más pequeño. N en la lína 93 es quien le indica en cuanto lo reduce

    desorden=puzzle.copy()
    union=puzzle.copy()
    
    desorden=desorden[n-m::,n-m::] # cojo el trozo de puzzle que quiero reducir y empieza a resolver.
    
    # for x in range(desorden.shape[1]):
        
    #     if x < desorden.shape[1]-2:
    #         while desorden[0][x] != (np.amin(desorden)+x):
                
    #             objetivo=np.amin(desorden)+x
    #             posicionMinimo = int(np.where(puzzle == objetivo)[0]), int(np.where(puzzle == objetivo)[1]) #posicion[0] -> Fila || posicion[1] -> Columna
                
    #             cero=np.max(puzzle)
    #             posicionCero = int(np.where(puzzle == cero)[0]), int(np.where(puzzle == cero[1])) #posicion[0] -> Fila || posicion[1] -> Columna
                
    #             while posicionMinimo[1] != x: #Voy a colocar el numero objetivo en la columna correspondiente
                    
    #                 if posicionCero[0] <= posicionMinimo[0]:
    #                     temp = desorden[posicionCero[0]][posicionCero[1]]
    #                     desorden[posicionCero[0]][posicionCero[1]] = desorden[posicionCero[0]+1][posicionCero[1]]
    #                     desorden[posicionCero[0]+1][posicionCero[1]] = temp
                    
    #                 elif posicionCero[0] > posicionMinimo[0]+1:
    #                     temp = desorden[posicionCero[0]][posicionCero[1]]
    #                     desorden[posicionCero[0]][posicionCero[1]] = desorden[posicionCero[0]-1][posicionCero[1]]
    #                     desorden[posicionCero[0]-1][posicionCero[1]] = temp
                
    #             while posicionMinimo[0] != 0: # Voy a subir el numero objetivo en la primera fila
    #                 pass
                    
                        

    union[n-m:,n-m:]=desorden
    puzzle=union.copy()

    showPuzzle(desorden)

    return puzzle

def columnSolver(puzzle,n,m):
    
    desorden=puzzle.copy()
    union=puzzle.copy()
    
    desorden=desorden[n-m+1::,n-m::]
    
    # for y in range(desorden.shape[0]):
    #     if y < desorden.shape[0]-2:
    #         while desorden[0][y] != (np.amin(desorden)+(y*desorden.shape[0])):
    #             pass  
    
    union[n-m+1:,n-m:]=desorden
    puzzle=union.copy()
    
    showPuzzle(desorden)
    
    return puzzle

def rotate2x2(puzzle):
    return puzzle # o devolvera un FALSE si no tiene solución

# main

n=0 #Defino n primero para que al entrar al bucle while se sepa el valor real de n 

while n<3 or n>10:
    n=int(input('Selecciona el número las dimensiones del puzzle (3-10): '))

numberList = list(range(1,(n*n)+1))
random.shuffle(numberList)
puzzle = np.reshape(numberList,(n,n)) ## np es el alias que le hemos dado a la libreria numpy (linea 3)

showPuzzle(puzzle)

m=n # m definirá en que punto de la resolución del puzzle nos encontramos

while m>2:
    rowSolver(puzzle,n,m)
    columnSolver(puzzle,n,m)
    m-=1

rotate2x2(puzzle)