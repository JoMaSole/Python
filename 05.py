if True:
    print("Deberia ejecutarse")

if False:
    print("al pedo escribo")


pet = input("Cual es tu mascota preferida?  ")

if (pet == "perro"):
    print("a mi tambien me gustan los perros")
elif (pet == "gato"):
    print("Vos sos re gato")
else:
    print("no conozco esa mascota")


stock = int(input("Digita el stock: "))
if stock >= 100 and stock <=1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto")

number = int(input("Ingrese un numero: "))
resultado = number % 2
if (resultado == 0):
    print("El numero es par")
else:
    print("El numero no es par")
