#Adivina el numero

import random

def adivinarNumero(min, max):
    return random.randint(min,max)

numero = adivinarNumero(1,15)
print(numero)