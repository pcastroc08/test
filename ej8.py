# Introducir dos números enteros y hacer suma, resta, producto, división y resto
# Introducir primer número
num1 = int(input("Introduce un número: "))
# Introducir segundo número
num2 = int(input("Introduce otro número: "))
# Hacer la suma
suma = num1 + num2
# Hacer la resta
resta = num1 - num2
# Hacer el producto
mult = num1 * num2
# Hacer la división
divi = num1 / num2
# Hacer el resto
resto = num1 % num2
# Mostrar el resultado
print(f"La suma es {suma}, la resta es {resta}, la multiplicación es {mult}, la división es {divi:.2f} y el resto es {resto}")