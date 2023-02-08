#Diccionarios

diccionario = {}
print(type(diccionario))

diccionario = {
    'avion': 'coso que vuela',
    'barco': 'coso que flota',
    'tren': 'coso que rueda',
    'numeros': 5
}

print(diccionario)
print(len(diccionario))

print(diccionario['barco']) #si no hay valor devuelve un error y se detiene el programa
print(diccionario.get('tren')) #si no hay valor devuelve NONE

print('avion' in diccionario) #devuelve true
print('coche' in diccionario) #devuelve false