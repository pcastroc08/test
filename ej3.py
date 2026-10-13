# Introducir tres números enteros. Hacer la multiplicación con los dos primeros y la división de este resultado con el tercer número
# Pedir primer número
num1 = int(input("Introduce un número: "))
# Pedir segundo número
num2 = int(input("Introduce otro número: "))
# Pedir tercer número
num3 = int(input("Introduce el último número: "))
# Hacer la multiplicación
mult = num1 * num2
# Mostrar el resutado de la multiplicación
print(f"El resultado de la multiplicación es: {mult}")
# Hacer la división
div = mult / num3
# Mostrar el resultado de la división
print(f"El resultado de la división es: {div:.2f}")
