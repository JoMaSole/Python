#ciclo for
'''
for element in range(1, 21): #se le puede dar comienzo y no incluye el ultimo valor
    print(element)
'''

lista = [1 , 25, 52, 84, 7]

for i in lista:
    print(i)

tupla = ('casa', 'auto', 'montaña')
for i in tupla:
    print(i)

producto = {
    'nombre': 'Camisa',
    'precio': 54,
    'stock': 15
}

for key in producto:
    print(key, ' ==> ', producto[key])
#esta es la forma correcta
for key, value in producto.items():
    print(key, ' ==> ', value)

personas = [
    {
        'name':'joan',
        'edad':32
    },
    {
        'name':'jaco',
        'edad':24
    },
    {
        'name':'bastian',
        'edad':7
    }
]
#se utiliza mucho para recorrer listas de productos
for p in personas:
    print('Nombre => ', p['name'],' Edad => ', p['edad'])
   # print('Edad => ', p['edad'])