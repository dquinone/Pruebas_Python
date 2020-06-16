import random
# Se crea plantilla de tablero con una lista de listas 
# Por medio de un for y un append se imprime en pantalla segun el rango
def ft_plantilla():
    plantilla = []
    for index in range(0,8):
        dato = [0,0,0,0,0,0,0,0]
        plantilla.append(dato)
    return plantilla
#Funcion para crear el movimiento de la pieza reina de arriba a abajo
# Y de derecha a izquierda creando una cruz en este caso con (1)
def ft_llenar_cruz(ar_plantilla, ar_movimiento, ar_index):
    for index in range(0,8):
        if ar_index == 'i':
            ar_plantilla[ar_movimiento][index] = 1
        else:
            ar_plantilla[index][ar_movimiento] = 1
    return ar_plantilla

def ft_move(ar_movimiento, ar_position = 'j'):
    state = False
#Validación de movimiento de la ficha tanto vertical como horizontal
#Se valida para saber la posición de la ficha 
#Retorna un estado boleano
    if ar_position == 'i':
        if  ar_movimiento - 1 >= 0: 
            state = True
    else:
        if ar_movimiento + 1 <= 7:
            state = True

    return state

def ft_move_reina(ar_plantilla, ar_move_aux_1,ar_move_aux_2, ar_move):

    #up and left
    if ar_move == 'up and left':
        while  ft_move(ar_move_aux_1, 'i') and ft_move(ar_move_aux_2):
            ar_plantilla[ar_move_aux_1 - 1 ][ar_move_aux_2 - 1] = 1
            ar_move_aux_1 = ar_move_aux_1 - 1
            ar_move_aux_2 = ar_move_aux_2 - 1 

    #up and right
    if ar_move == 'up and right':
        while  ft_move(ar_move_aux_1, 'i') and ft_move(ar_move_aux_2):
            ar_plantilla[ar_move_aux_1 - 1 ][ar_move_aux_2 + 1] = 1
            ar_move_aux_1 = ar_move_aux_1 - 1
            ar_move_aux_2 = ar_move_aux_2 + 1 

    #down and left
    if ar_move == 'down and left':
        while  ft_move(ar_move_aux_1, 'j') and ft_move(ar_move_aux_2, 'i'):
            ar_plantilla[ar_move_aux_1 + 1 ][ar_move_aux_2 - 1] = 1
            ar_move_aux_1 = ar_move_aux_1 + 1
            ar_move_aux_2 = ar_move_aux_2 - 1 

    #down and right   
    if ar_move == 'down and right':
        while  ft_move(ar_move_aux_1, 'j') and ft_move(ar_move_aux_2, 'j'):
            ar_plantilla[ar_move_aux_1 + 1 ][ar_move_aux_2 + 1] = 1
            ar_move_aux_1 = ar_move_aux_1 + 1
            ar_move_aux_2 = ar_move_aux_2 + 1 

def execute():
    movimiento_1 = random.randint(0, 7)
    movimiento_2 = random.randint(0, 7)
    plantilla = ft_plantilla()
    list_move = ['up and left', 'up and right', 'down and left' , 'down and right']
   
    ft_llenar_cruz(plantilla, movimiento_1, 'i')
    ft_llenar_cruz(plantilla, movimiento_2, 'j')

    for index in list_move:
        ft_move_reina(plantilla, movimiento_1, movimiento_2, index)

    plantilla[movimiento_1][movimiento_2] = 8

    for index in range(0,8):
        print(plantilla[index])

execute()

