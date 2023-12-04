def partida_ajedrez(fichero):
    # Se utiliza \t para separar las columnas y \n para separar las filas.
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    print(tablero_inicial)

    # Lista vacía para añadir las filas del tablero
    tablero = []

    # Se utiliza un bucle para recorrer las filas y columnas del tablero inicial.
    for i in tablero_inicial.split('\n'):
        # Toma la cadena i y la divide en subcadenas cada vez que encuentra un carácter de tabulación (\t). 
        # Esto devuelve una lista de subcadenas resultantes.
        tablero.append(i.split('\t'))

    # Preguntar al usuario por el nombre del archivo.
    nombre_archivo = input('Introduce el nombre del archivo para guardar el tablero inicial: ')

    # Abrir el archivo en modo escritura.
    with open(nombre_archivo, 'w') as f:
        # Bucle iterativo para recorrer las filas del tablero.
        # i toma como valores cada una de las listas (filas) del tablero.
        for i in tablero:
            # Escribimos cada fila en una línea concatenando los caracteres que contiene.
            f.write('\t'.join(i) + '\n')

    print(f'Tablero inicial guardado en el archivo: {nombre_archivo}')

    # Empieza la partida inicializando un contador de movimientos a cero.
    movimiento = 0
    # Bucle condicional para realizar movimientos en la partida hasta que el usuario decida terminar.
    while True:
        # Preguntar al usuario si quiere realizar otro movimiento.
        continuar = input('Deseas hacer un movimiento (s/n): ')
        # Condicional para ver si el usuario ha respondido si.
        if continuar != 's':
            # Si el usuario no ha contestado que si, salimos del bucle condicional para terminar la partida.
            break
        else:
            # Si el usuario quiere hacer un movimiento preguntamos por las coordenadas de las casillas de origen y destino.
            fila_principio = int(input('Introduce la fila de la pieza que quieras mover: '))
            columna_principio = int(input('Introduce la columna de la pieza que quieras mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destino: '))
            # Hacemos el movimiento en el tablero
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_principio-1][columna_principio-1]
            tablero[fila_principio-1][columna_principio-1] = ''
            # Incrementamos el contador de movimientos en 1.
            movimiento += 1
            # Abrimos el fichero en modo añadir.
            with open(fichero, 'a') as f:
                # Añadimos una cadena con el número de movimiento.
                f.write('Movimiento' + str(movimiento) + '\n')
                # Bucle iterativo para recorrer las filas del tablero.
                # i toma como valores cada una de las listas (filas) del tablero.
                for i in tablero:
                    f.write('\t'.join(i) + '\n')

    print('Partida finalizada.')

# Llamar a la función para ejecutar el código.
partida_ajedrez("partidas.txt")