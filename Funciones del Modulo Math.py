from cmath import log, pi
import math

factorial = math.factorial(4)
print('el factorial es', factorial)

raiz = math.sqrt(4)
print('la raiz de 4 es', raiz)

a = math.floor(3.7)
print('redondea hacia abajo', a)

b = math.ceil(3.1)
print('redondea hacia arriba', b)

phi = math.pi
print('phi es:', phi)

print(math.sin(45))

# Grados pasados a radianes
grados= 45
angulo = grados * 2* math.pi / 360.0
print(math.sin(angulo))

s = math.cos(angulo + math.pi/2)
print('Un modulo dentro de otro modulo:', s)


funcion_pow = math.pow(4,2)
print('El valor de un número x elevado a la potencia:', funcion_pow)

print('Es lo mismo que hacer 4**2:', 4**2)

