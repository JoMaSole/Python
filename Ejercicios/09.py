# crud crear, leer, cambiar, eliminar

numeros = [1, 2, 3, 4, 5]
print(numeros[2])
numeros[-1] = 8
print(numeros)

#agregar un nuevo elemento
#por defecto lo agriga al final de la lista
numeros.append(400)
print(numeros)

#inserto (no elimino) el nuevo valor, primero indicando la posicion y luego el valor
numeros.insert(0, 'holis')
print(numeros)

numeros.insert(3, 'change')
print(numeros)

tareas = ['primero', 'segundo', 'tercero']
new_list = numeros + tareas
print(new_list)

index = new_list.index('segundo')
new_list[index] = 'cambiado'
print(new_list)

#eliminar elementos
new_list.remove('primero')
print(new_list)

new_list.pop(0)  #elimina el ultimo elemento por defecto, se le puede indicar la pocision
print(new_list)

new_list.reverse()
print(new_list)

#ordenar listas // no funciona con tipos de listas mezcladas
num = [15,8,12,4]
num.sort()
lista = ['un', 'do', 'tre', 'al']
lista.sort()
print(num)
print(lista)

