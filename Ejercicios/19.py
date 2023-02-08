#funciones y alcance de las funciones
'''
def <nombre>(<parametros>):
    <cuerpo>
    return <expresion>
'''

def suma(a,b):
    total = a + b
    return total

suma(2,3)

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

nombre_completo('Joan', 'Solé')
nombre_completo('Joan', 'Solé', inverso = True)
nombre_completo(apellido = 'Solé', nombre = 'Joan')
