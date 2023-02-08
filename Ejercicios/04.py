x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

y_str = format(y, ".2g")
print("str = ", y_str)
print(y_str == str(x))

# Imprime x cantidad de veces el string
print("*" * 10)

tolerance = 0.00001
# abs  valor absoluto para que siempre de positivo
print(abs(x - y) < tolerance)
