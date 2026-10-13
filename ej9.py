# Calcular la hipotenusa de un triángulo rectángulo
# Importar variables
import math
# Pedir cateto A
cata = float(input("Introduce un cateto: "))
# Pedir cateto B
catb = float(input("Introduce el segundo cateto: "))
# Calcular hipotenusa
hipotenusa = math.sqrt(cata**2 + catb**2)
# Mostrar resultado
print(f"La hipotenusa es: {hipotenusa:.2f}")