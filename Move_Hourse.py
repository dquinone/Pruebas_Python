import random
# Se crea plantilla de tablero con una lista de listas 
# Por medio de un for y un append se imprime en pantalla segun el rango

def ft_plantilla():
    plantilla = []
    for index in range(0,8):
        dato = [0,0,0,0,0,0,0,0]
        plantilla.append(dato)
    return plantilla
# Función para validar el movimiento y la posición del caballo en el tablero
# Se evalua por medio de un boleano para verificar si se puede o no hacer el movimiento

def ft_move_caballo(ar_move, ar_position, ar_operador = ''):
    state  = False
    # up and left
    if ar_move == 1:
        if ar_position - 2 >= 0:
            state  = True
    # down and rigth
    elif ar_move == 2:
        if ar_position + 2 <= 7:
            state  = True
    elif ar_move == 3:
        if ar_operador == 'right':
            if ar_position + 1 <= 7:
                state = True
        elif ar_operador == 'left':
            if ar_position - 1 >= 0:  
                state = True
    return state
# Función para validar el movimiento de la pieza e imprmir (8) para el caballo
# Y 1 para identificar los movimientos segun la función del movimiento del caballo
# Se retorna la plantilla con los movimientos (1) y la posición de la pieza (8)

def ft_move_piece_caballo(plantilla, movimiento_1, movimiento_2):
    plantilla[movimiento_1][movimiento_2] = 8
    # up_left (arriba e izquierda)
    if ft_move_caballo(3 if ft_move_caballo(1, movimiento_1) else 0, movimiento_2, 'left'):
        plantilla[movimiento_1 - 2][movimiento_2 - 1] = 1
    # up_right (arriba y derecha)
    if ft_move_caballo(3 if ft_move_caballo(1, movimiento_1) else 0, movimiento_2, 'right'):
        plantilla[movimiento_1 - 2][movimiento_2 + 1] = 1
    # down_left (abajo e izquierda)
    if ft_move_caballo(3 if ft_move_caballo(2, movimiento_1) else 0, movimiento_2, 'left'):
        plantilla[movimiento_1 + 2][movimiento_2 - 1] = 1
    # down_right (abajo y derecha)
    if ft_move_caballo(3 if ft_move_caballo(2, movimiento_1) else 0, movimiento_2, 'right'):
        plantilla[movimiento_1 + 2][movimiento_2 + 1] = 1
    # left_up (izquierda y arriba)
    if ft_move_caballo(3 if ft_move_caballo(1, movimiento_2) else 0, movimiento_1, 'left'):
        plantilla[movimiento_1 - 1][movimiento_2 - 2] = 1
    # left_down (izquierda y abajo)
    if ft_move_caballo(3 if ft_move_caballo(1, movimiento_2) else 0, movimiento_1, 'right'):
        plantilla[movimiento_1 + 1][movimiento_2 - 2] = 1
    # right_up (derecha y arriba)
    if ft_move_caballo(3 if ft_move_caballo(2, movimiento_2) else 0, movimiento_1, 'left'):
        plantilla[movimiento_1 - 1][movimiento_2 + 2] = 1
    # right_down (derecha y abajo)
    if ft_move_caballo(3 if ft_move_caballo(2, movimiento_2) else 0, movimiento_1, 'right') :
        plantilla[movimiento_1 + 1][movimiento_2 + 2] = 1
    return plantilla

# Impresión de movimietos en la plantilla segun un rango creado de forma random
def execute():
    movimiento_1 = random.randint(0, 7)
    movimiento_2 = random.randint(0, 7)
    print(movimiento_1,movimiento_2)
    for index in range(0,8):
        print(ft_move_piece_caballo(ft_plantilla(), movimiento_1, movimiento_2)[index])

execute()