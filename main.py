ingreso = input("Seleccionar opcion, 'piedra', 'papel', 'tijera': ")
user_option = ingreso.lower()
computer_option = 'piedra'
puntaje_user = 0
puntaje_cpu = 0

if user_option == computer_option:
    print("Empate!")
elif user_option == 'piedra':
    if (computer_option == 'tijera'):
        print("Piedra le gana a tijera")
        print("Bien! Ganaste 1 punto")
        puntaje_user = puntaje_user + 1
        print(f"Puntajes: usuario={puntaje_user} cpu= {puntaje_cpu}")
    else:
        print("Papel le gana a piedra")
        print("Perdiste un punto")
        puntaje_user = puntaje_user - 1
        print(f"Puntajes: usuario={puntaje_user} cpu= {puntaje_cpu}")

elif user_option == 'papel':
    if (computer_option == 'piedra'):
        print("Papel le gana a piedra")
        print("Bien! Ganaste 1 punto")
        puntaje_user = puntaje_user + 1
        print(f"Puntajes: usuario= {puntaje_user} cpu= {puntaje_cpu}")
    else:
        print("Tijera le gana a papel")
        print("Perdiste un punto")
        puntaje_user = puntaje_user - 1
        print(f"Puntajes: usuario={puntaje_user} cpu= {puntaje_cpu}")

elif user_option == 'tijera':
    if (computer_option == 'papel'):
        print("Tijera le gana a papel")
        print("Bien! Ganaste 1 punto")
        puntaje_user = puntaje_user + 1
        print(f"Puntajes: usuario= {puntaje_user} cpu={puntaje_cpu}")
    else:
        print("Piedra le gana a tijera")
        print("Perdiste un punto")
        puntaje_user = puntaje_user - 1
        print(f"Puntajes: usuario={puntaje_user} cpu={puntaje_cpu}")

