#tuplas
numeros = (78,1,2,3,4)
strings = ('inicio', 'seguido', 'tercero', 'inicio')
print(type(numeros))
print('pocicion primera', numeros[0])

# Crud
#las tuplas no pueden ser modificadas // son solo lectura

print(strings.index('seguido'))
print(strings.count('inicio'))

#convertir tupla a lista
my_list = list(strings)
print(type(my_list))

my_tuple = tuple(my_list)
print(type(my_tuple))
