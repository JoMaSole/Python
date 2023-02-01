my_name = "Joan"
my_age = 32
my_lastname = "Solé"

completo = "Hola mi nombre es " + my_name + " y mi apellido es " + my_lastname
print(completo)

completito = "Hola mi nombre es {} y mi apellido es {}".format(my_name, my_lastname)
print(completito)

#esta es la version mas utilizada
otraversion = f"Hola mi nombre es {my_name} {my_lastname} y tengo {my_age}"
print(otraversion)
