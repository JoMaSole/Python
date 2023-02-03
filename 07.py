text = "Ya sabe programar en Python"
print(text[0]) #devuelve el caracter solicitado en la pocicion
size = len(text)
print(text[size - 1])
print(text[-2])

print(text[8:17])#imprime esa interseccion
print(text[:10])#desde el principio al 10
print(text[5:])#desde la posicion 5 al final
print(text[:])#va del principio al fin
print(text[5:17:2]) #el tercero indica los saltos
print(text[::3])#el tercero indica los saltos
