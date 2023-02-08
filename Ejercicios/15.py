#ciclos anidados

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#print(matriz[0][1]) # esto devuelve una lista [fila][columna]

for row in matriz:
    print(row)
    for col in row:
        print(col)