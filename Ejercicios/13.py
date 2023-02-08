#While
'''
while True:
    print('ejecutado')

counter = 0

while counter < 10: #mientras counter sea menor a 10 se va a ejecutar
    counter += 1
    print(counter)
'''
'''
counter = 0

while counter < 20:
    counter += 1
    # print(counter) #en esta posicion imprime hasta el 15 inclusive
    if counter == 15:
        break
    print(counter) #en esta posicion imprime hasta el 14 inclusive
'''
counter = 0

while counter < 20:
    counter += 1
    if counter < 15: #imprime a partir de esa condicion
        continue
    print(counter) # este print no se va a ejecutar hasta que el counter valga 15