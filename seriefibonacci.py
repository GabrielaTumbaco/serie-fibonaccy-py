# Cantidad de términos que queremos en la serie de Fibonacci
limite = 10

# Inicializamos los primeros dos términos
a, b = 0, 1

print("Serie de Fibonacci hasta el término", limite, ":")

# Bucle para imprimir la serie de Fibonacci
for _ in range(limite):
    print(a, end=" ")
    # Calculamos el siguiente término
    a, b = b, a + b

print()  # Nueva línea al final