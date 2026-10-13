# Introducir una letra en minúscula y convertirla en mayúscula
# Pedir letra
letra = str(input("Introduce una letra minúscula: "))
# Pasarla a ASCII
ascii_letra = ord(letra)
# Pasar ASCII a letra mayúscula
ascii_mayuscula = ascii_letra - 32
# Pasar ASCII mayúscula a texto
resultado = chr(ascii_mayuscula)
# Mostrar el resultado
print(f"La letra en mayúscula es {resultado}")