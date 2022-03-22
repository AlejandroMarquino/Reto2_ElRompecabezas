import string
import random

if __name__ == '__main__':
    piece=()
    move = 0
    empty_space=()
    list1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#he importado la librería random para que desordene aleatoriamente la lista de números

random.shuffle(list1)
print('\n'*2)

matrix=[]
while list1 !=[]: # transformar la lista en una matriz 4x4
    matrix.append(list1[:4])
    list1 = list1[4:]

#busqueda del hueco en la matriz que sería el 0.
for x in range (len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == 0:
            empty_space = (x,y)

print()

#saca por pantalla la lista como una matriz y el :02d es para que tenga dos dígitos.
while True:
    print('\n+----+----+----+---|')

    for x in range (len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:

                print('| |' , end='  ')
            else:
                 print('|' + '{:02d}' .format(matrix[x][y]), end='  ')

        print('\n+----+----+----+---|')

    # Aquí hago cuanto el usuario tiene que hacer movimiento y le doy la opción de salir del juego con 'S"
    num = input('\nIndique la ficha que desea mover : ( q ) para salir del juego. ')
    if num in ['s','S']:
        break
    num = int(num)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if num == matrix[i][j]:
                piece = (i,j)

    if num > 15:
        print('no se puede realizar ese movimiento  ')
    else:

        if(empty_space==(piece[0]-1,piece[1]))\
           or(empty_space==(piece[0]+1,piece[1]))\
           or(empty_space==(piece[0],piece[1]-1))\
           or(empty_space==(piece[0],piece[1]+1)):
            matrix[empty_space[0]][empty_space[1]]=num
            matrix[piece[0]][piece[1]]=0
            empty_space=(piece[0],piece[1])
            move = move +1
            print()
            print('has hecho ',move , 'movimientos extra ')
            print(2*'\n')
        else:
            print('no se puede realizar ese movimiento, prueba de nuevo ')

print('game over  ')

