# int Integer 

numeroEntero = 2

#float Numero decimal

numDecimal = 0,800

# complex Numero complejo

numComplejo = 5+8j

print(numeroEntero)
print(type(numeroEntero))

print(numDecimal)
print(type(numDecimal))

print(numComplejo)
print(type(numComplejo))

#Cast
decimaldeentero = float(numeroEntero)
enterodedecimal = int(numDecimal)

#Random

import random  # noqa: E402
rng = random.randrange(1,10) # No incluye 10
rngpar = random.randrange(2,11,2)
rngimpar = random.randrange(1,10,2)

print(rng)
print(rngpar)
print(rngimpar)