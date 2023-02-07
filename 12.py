#declaracion de un diccionario declarando una persona
persona = {
    'nombre' : 'Joan',
    'apellido' : 'Sole',
    'dni' : 35269534,
    'edad': 32,
    'lenguajes' : ['php', 'python']
}

print(persona)

persona['nombre'] = 'Jaco'
persona['edad'] -= 8
persona['lenguajes'].append('html')
print(persona)

#borrar atributo
del persona['dni']
persona.pop('apellido')
print(persona)

print(persona.items())
print(persona.keys())
print(persona.values())
