def primera_letra(lista_de_palabras):
    primera_letra = []

    for palabra in lista_de_palabras:
        #dar una expresion booleana y responder un mensaje cuando la assercion no funciona, caso contrario continua el programa
        assert type(palabra) == str, f'{palabra} no es un string'
        assert len(palabra) > 0, 'No se permiten string vacios'

        primera_letra.append(palabra[0])
    
    return primera_letra