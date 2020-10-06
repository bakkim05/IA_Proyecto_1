
def black_move(matrix, moves):
    num_black = 0 # Numero de fichas negras en el tablero
    new_matrix = matrix # Matriz a actualizar
    old_x = 0 # Posicion x anterior de la ficha a mover
    old_y = 0 # Posicion y anterior de la ficha a mover
    flag = 5 # Bandera para saber que tipo de movimiento se va a realizar

    best_x = 0 # Posicion x de la mejor ficha a mover
    best_y = 0 # Posicion y de la mejor ficha a mover

    evalu = False
    
    for i in range(2):
        for fichas in new_matrix[i]:
            print(fichas)
            if fichas == 2:
                num_black += 1;
                
    if num_black == 0: # Movida inicial, no hay fichas en el tablero
        print("movida inicial")
        old_x = 0
        old_y = 4
        if moves == 1:
            new_matrix[0][3] = 2
            flag = 1
            best_x = 0 
            best_y = 3
        elif moves == 2:
            new_matrix[0][2] = 2
            flag = 1
            best_x = 0 
            best_y = 2
        elif moves == 3:
            new_matrix[0][1] = 2
            flag = 1
            best_x = 0 
            best_y = 1
        elif moves == 4:
            new_matrix[0][0] = 2
            flag = 3
            best_x = 0 
            best_y = 0
            
    else: #hay fichas en el tablero
        print("ya hay ficha")
        # Logica para evaluar las primeras 4 casillas del tablero (0,3 0,2 0,1 0,0)
        if new_matrix[0][3] == 2 and moves == 4:
            if new_matrix[1][0] == 3:
                old_x = 0
                old_y = 3
                flag = 0
                best_x = 1
                best_y = 0
                evalu = True

        elif new_matrix[0][2] == 2 and moves == 4:
            if new_matrix[1][1] == 3:
                old_x = 0
                old_y = 2
                flag = 0
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][2] == 2 and moves == 3:
            if new_matrix[1][0] == 3:
                old_x = 0
                old_y = 2
                flag = 0
                best_x = 1
                best_y = 0
                evalu = True

        elif new_matrix[0][1] == 2 and moves == 4:
            if new_matrix[1][2] == 3:
                old_x = 0
                old_y = 1
                flag = 0
                best_x = 1
                best_y = 2
                evalu = True
        elif new_matrix[0][1] == 2 and moves == 3:
            if new_matrix[1][1] == 3:
                old_x = 0
                old_y = 1
                flag = 0
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][1] == 2 and moves == 2:
            if new_matrix[1][0] == 3:
                old_x = 0
                old_y = 1
                flag = 0
                best_x = 1
                best_y = 0
                evalu = True    
            
        elif new_matrix[0][0] == 2 and moves == 3:
            if new_matrix[1][2] == 3:
                old_x = 0
                old_y = 0
                flag = 0
                best_x = 1
                best_y = 2
                evalu = True
        elif new_matrix[0][0] == 2 and moves == 2:
            if new_matrix[1][1] == 3:
                old_x = 0
                old_y = 0
                flag = 0
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][0] == 2 and moves == 1:
            if new_matrix[1][0] == 3:
                old_x = 0
                old_y = 0
                flag = 0
                best_x = 1
                best_y = 0
                evalu = True

        #Lógica para casillas especiales
        elif new_matrix[0][3] == 2 and moves == 3:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 3
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True

        elif new_matrix[0][2] == 2 and moves == 2:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 2
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True
        elif new_matrix[0][1] == 2 and moves == 1:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 1
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True
                
        elif new_matrix[0][0] == 2 and moves == 4:
            if new_matrix[1][3] == 0:
                old_x = 0
                old_y = 0
                flag = 3
                best_x = 1
                best_y = 3
                evalu = True
                
        #Logica para movimientos normales
        elif new_matrix[0][3] == 2 and moves == 4:
            if new_matrix[1][0] == 0:
                old_x = 0
                old_y = 3
                flag = 4
                best_x = 1
                best_y = 0
                evalu = True
        elif new_matrix[0][3] == 2 and moves == 3:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 3
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True
        elif new_matrix[0][3] == 2 and moves == 2:
            if new_matrix[0][1] == 0:
                old_x = 0
                old_y = 3
                flag = 4
                best_x = 0
                best_y = 1
                evalu = True
        elif new_matrix[0][3] == 2 and moves == 1:
            if new_matrix[0][2] == 0:
                old_x = 0
                old_y = 3
                flag = 4
                best_x = 0
                best_y = 2
                evalu = True

        elif new_matrix[0][2] == 2 and moves == 4:
            if new_matrix[1][1] == 0:
                old_x = 0
                old_y = 2
                flag = 4
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][2] == 2 and moves == 3:
            if new_matrix[1][0] == 0:
                old_x = 0
                old_y = 2
                flag = 4
                best_x = 1
                best_y = 0
                evalu = True
        elif new_matrix[0][2] == 2 and moves == 2:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 2
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True
        elif new_matrix[0][2] == 2 and moves == 1:
            if new_matrix[0][1] == 0:
                old_x = 0
                old_y = 2
                flag = 4
                best_x = 0
                best_y = 1
                evalu = True
                
        elif new_matrix[0][1] == 2 and moves == 4:
            if new_matrix[1][2] == 0:
                old_x = 0
                old_y = 1
                flag = 4
                best_x = 1
                best_y = 2
                evalu = True
        elif new_matrix[0][1] == 2 and moves == 3:
            if new_matrix[1][1] == 0:
                old_x = 0
                old_y = 1
                flag = 4
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][1] == 2 and moves == 2:
            if new_matrix[1][0] == 0:
                old_x = 0
                old_y = 1
                flag = 4
                best_x = 1
                best_y = 0
                evalu = True   
        elif new_matrix[0][1] == 2 and moves == 1:
            if new_matrix[0][0] == 0:
                old_x = 0
                old_y = 1
                flag = 3
                best_x = 0
                best_y = 0
                evalu = True
                
        elif new_matrix[0][0] == 2 and moves == 4:
            if new_matrix[1][3] == 0:
                old_x = 0
                old_y = 0
                flag = 3
                best_x = 1
                best_y = 3
                evalu = True
        elif new_matrix[0][0] == 2 and moves == 3:
            if new_matrix[1][2] == 0:
                old_x = 0
                old_y = 0
                flag = 4
                best_x = 1
                best_y = 2
                evalu = True
        elif new_matrix[0][0] == 2 and moves == 2:
            if new_matrix[1][1] == 0:
                old_x = 0
                old_y = 0
                flag = 4
                best_x = 1
                best_y = 1
                evalu = True
        elif new_matrix[0][0] == 2 and moves == 1:
            if new_matrix[1][0] == 0:
                old_x = 0
                old_y = 0
                flag = 4
                best_x = 1
                best_y = 0
                evalu = True

        for i in range(2):
            for j in range(8):
                if new_matrix[i][j] == 2: # Hay una ficha negra en la posicion evaluada
                # Logica utilizada para evaluar si existe una ficha capaz de salir del tablero
                    if i == 1 and j == 6 and moves == 4:
                        old_x = 1
                        old_y = 6
                        flag = 2
                        evalu = True
                    elif i == 1 and j == 7 and moves == 3:
                        old_x = 1
                        old_y = 7
                        flag = 2
                        evalu = True
                    elif i == 0 and j == 7 and moves == 2:
                        old_x = 0
                        old_y = 7
                        flag = 2
                        evalu = True
                    elif i == 0 and j == 6 and moves == 1:
                        old_x = 0
                        old_y = 6
                        flag = 2
                        evalu = True

                # Logica para evaluar si existe una ficha que se pueda comer
                    # Ficha blanca en posicion 1,0 y ficha negra en fila superior
                    if i == 0 and j == 3 and moves == 4 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 2 and moves == 3 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 1 and moves == 2 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 0 and moves == 1 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 0
                            evalu = True
                    # Ficha blanca en posicion 1,1 y ficha negra en fila superior
                    elif i == 0 and j == 2 and moves == 4 and evalu == False:
                        if new_matrix[1][1] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 1 and moves == 3 and evalu == False:
                        if new_matrix[1][1] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 0 and moves == 2 and evalu == False:
                        if new_matrix[1][1] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 1
                            evalu = True
                    # Ficha blanca en posicion 1,2 y ficha negra en fila superior
                    elif i == 0 and j == 1 and moves == 4 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 2
                            evalu = True
                    elif i == 0 and j == 0 and moves == 3 and evalu == False:
                        if new_matrix[1][0] == 3:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = 1
                            best_y = 2
                            evalu = True
                    # Demas opciones para comer
                    elif j+moves < 8:
                        if new_matrix[i][j+moves] == 3 and evalu == False:
                            old_x = i
                            old_y = j
                            flag = 0
                            best_x = i
                            best_y = j+moves
                            evalu = True

                # Logica para evaluar si se puede llegar a una casilla segura
                    # Si se tiene una ficha negra en posicion 0,3 y se mueve 4 posiciones
                    if i == 0 and j == 3 and moves == 3 and evalu == False:
                        if new_matrix[0][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 0
                            evalu = True
                    # Si se tiene una ficha negra en posicion 0,2 y se mueve 4 posiciones
                    elif i == 0 and j == 2 and moves == 2 and evalu == False:
                        if new_matrix[0][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 0
                            evalu = True
                    # Si se tiene una ficha negra en posicion 0,1 y se mueve 4 posiciones
                    elif i == 0 and j == 1 and moves == 1 and evalu == False:
                        if new_matrix[0][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 0
                            evalu = True
                    # Si se tiene una ficha negra en posicion 0,0 y se mueve 4 posiciones
                    elif i == 0 and j == 0 and moves == 4 and evalu == False:
                        if new_matrix[1][3] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 1
                            best_y = 3
                            evalu = True
                    # Si se tiene una ficha en las posiciones 1,5 1,6 1,7 0,7
                    elif i == 1 and j == 5 and moves == 4 and evalu == False:
                        if new_matrix[0][6] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 6
                            evalu = True
                    elif i == 1 and j == 6 and moves == 3 and evalu == False:
                        if new_matrix[0][6] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 6
                            evalu = True
                    elif i == 1 and j == 7 and moves == 2 and evalu == False:
                        if new_matrix[0][6] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 6
                            evalu = True
                    elif i == 0 and j == 7 and moves == 1 and evalu == False:
                        if new_matrix[0][6] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 0
                            best_y = 6
                            evalu = True
                    # Los demas casos para llegar a la casilla del medio
                    elif i == 1 and j == 0 and moves == 3 and evalu == False:
                        if new_matrix[1][3] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 1
                            best_y = 3
                            evalu = True
                    elif i == 1 and j == 1 and moves == 2 and evalu == False:
                        if new_matrix[1][3] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 1
                            best_y = 3
                            evalu = True
                    elif i == 1 and j == 2 and moves == 1 and evalu == False:
                        if new_matrix[1][3] == 0:
                            old_x = i
                            old_y = j
                            flag = 3
                            best_x = 1
                            best_y = 3
                            evalu = True

                # Logica para realizar movimientos normales
                    # Movimientos para la ficha en la casilla 0,3
                    if i == 0 and j == 3 and moves == 1 and evalu == False:
                        if new_matrix[0][2] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 2
                            evalu = True
                    elif i == 0 and j == 3 and moves == 2 and evalu == False:
                        if new_matrix[0][1] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 3 and moves == 4 and evalu == False:
                        if new_matrix[1][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 0
                            evalu = True
                    # Movimientos para la ficha en la casilla 0,2
                    if i == 0 and j == 2 and moves == 1 and evalu == False:
                        if new_matrix[0][1] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 2 and moves == 3 and evalu == False:
                        if new_matrix[1][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 2 and moves == 4 and evalu == False:
                        if new_matrix[1][1] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 1
                            evalu = True
                    # Movimientos para la ficha en la casilla 0,1
                    elif i == 0 and j == 1 and moves == 2 and evalu == False:
                        if new_matrix[1][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 1 and moves == 3 and evalu == False:
                        if new_matrix[1][1] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 1 and moves == 4 and evalu == False:
                        if new_matrix[1][2] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 2
                            evalu = True
                    # Movimientos para la ficha en la casilla 0,0
                    elif i == 0 and j == 0 and moves == 1 and evalu == False:
                        if new_matrix[1][0] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 0
                            evalu = True
                    elif i == 0 and j == 0 and moves == 2 and evalu == False:
                        if new_matrix[1][1] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 1
                            evalu = True
                    elif i == 0 and j == 0 and moves == 3 and evalu == False:
                        if new_matrix[1][2] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = 2
                            evalu = True
                    # Movimientos en la fila 1
                    elif j+moves < 8:
                        if new_matrix[1][j+moves] == 0 and evalu == False:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 1
                            best_y = j+moves
                            evalu = True
                    # Movimientos para las fichas que se muevan hacia la fila 0
                    elif i == 1 and j == 4 and moves == 4 and evalu == False:
                        if new_matrix[0][7] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 7
                            evalu = True
                    elif i == 1 and j == 5 and moves == 3 and evalu == False:
                        if new_matrix[0][7] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 7
                            evalu = True
                    elif i == 1 and j == 6 and moves == 2 and evalu == False:
                        if new_matrix[0][7] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 7
                            evalu = True
                    elif i == 1 and j == 7 and moves == 1 and evalu == False:
                        if new_matrix[0][7] == 0:
                            old_x = i
                            old_y = j
                            flag = 4
                            best_x = 0
                            best_y = 7
                            evalu = True

                # Logica cuando no se puede realizar ninguno de los movimientos anteriormente evaludaos, se procede a sacar una nueva ficha
                    elif evalu == False:
                        old_x = 0
                        old_y = 4
                        if moves == 1:
                            new_matrix[0][3] = 2
                            flag = 1
                            evalu = True
                        elif moves == 2:
                            new_matrix[0][2] = 2
                            flag = 1
                            evalu = True
                        elif moves == 3:
                            new_matrix[0][1] = 2
                            flag = 1
                            evalu = True
                        elif moves == 4:
                            new_matrix[0][0] = 2
                            flag = 3
                            evalu = True
                            
        #Logica para la ultimas 2 casillas
        if new_matrix[0][7] == 2 and moves == 2:
            old_x = 0
            old_y = 7
            flag = 2
            evalu = True
        elif new_matrix[0][6] == 2 and moves == 1:
            old_x = 0
            old_y = 6
            flag = 2
            evalu = True
        elif new_matrix[0][7] == 2 and moves == 1 and evalu == False:
            if new_matrix[0][6] == 0:
                old_x = 0
                old_y = 7
                flag = 3
                evalu = True
                best_x = 0
                best_y = 6

        if old_x == 0 and old_y == 4:
            new_matrix[best_x][best_y] = 2
        elif flag == 2:
            new_matrix[old_x][old_y] = 0
        else:
            new_matrix[best_x][best_y] = 2
            new_matrix[old_x][old_y] = 0
                            
    return new_matrix, flag, old_x, old_y

