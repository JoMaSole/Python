objetivo = int(input('Escoge un numero entero: '))
respuesta = 0

while respuesta**2 < objetivo: #**2 significa: al cuadrado
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'El numero elegido {objetivo} no tiene una raiz exacta')
