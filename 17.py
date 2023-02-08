#algoritmo de aproximacion

objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0
#abs() regresa el valor absoluto
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    
if abs(respuesta**2 - objetivo >= epsilon):
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

#con numeros muy grandes se cuelga jajajaja