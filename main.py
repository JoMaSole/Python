import random

options = ('piedra', 'papel', 'tijera')
puntaje_user = 0
puntaje_cpu = 0
continuar = True

while continuar == True:
    ingreso = input("Seleccionar opcion, 'piedra', 'papel', 'tijera': ")
    user_option = ingreso.lower()

    if (not user_option in options):
        print('Esa opcion no es valida')

    computer_option = random.choice(options)

    print('Opcion del usuario = ', user_option)
    print('Opcion del CPU = ', computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == 'piedra':
        if (computer_option == 'tijera'):
            print("Piedra le gana a tijera")
            print("Bien! Ganaste 1 punto")
            puntaje_user = puntaje_user + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")
        else:
            print("Papel le gana a piedra")
            print("Perdiste un punto")
            puntaje_cpu = puntaje_cpu + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")

    elif user_option == 'papel':
        if (computer_option == 'piedra'):
            print("Papel le gana a piedra")
            print("Bien! Ganaste 1 punto")
            puntaje_user = puntaje_user + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")
        else:
            print("Tijera le gana a papel")
            print("Perdiste un punto")
            puntaje_cpu = puntaje_cpu + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")

    elif user_option == 'tijera':
        if (computer_option == 'papel'):
            print("Tijera le gana a papel")
            print("Bien! Ganaste 1 punto")
            puntaje_user = puntaje_user + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")
        else:
            print("Piedra le gana a tijera")
            print("Perdiste un punto")
            puntaje_cpu = puntaje_cpu + 1
            print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")

    puntaje_user = puntaje_user
    puntaje_cpu = puntaje_cpu
    seguir = input('Desea seguir jugando? (si , no): ')
    seguir = seguir
    # print(seguir)
    # break
    if seguir != 'si' and seguir != 'no':
        while seguir != 'si' or seguir != 'no':
            print('Por favor ingrese una opcion valida (si , no)')
            seguir = input('')
            if seguir == 'si':
                break
            elif seguir == 'no':
                break
        
    if seguir == 'si':
        continuar = True
    elif seguir == 'no':
        break