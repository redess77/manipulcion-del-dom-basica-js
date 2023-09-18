import random

# Lista de palabras para el juego
palabras = ["constitucion", "papelon", "pumporo", "netflix", "blacklist"]

# Función para elegir una palabra al azar
def elegir_palabra():
    return random.choice(palabras)

# Función para jugar al ahorcado
def jugar_ahorcado():
    palabra = elegir_palabra()
    palabra_adivinada = "_" * len(palabra)
    intentos_maximos = 6
    letras_adivinadas = []
    
    print("¡Bienvenido al juego del ahorcado!")
    
    while intentos_maximos > 0:
        print("\nPalabra a adivinar:", " ".join(palabra_adivinada))
        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            print("¡Correcto! La letra está en la palabra.")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_adivinada = palabra_adivinada[:i] + letra + palabra_adivinada[i+1:]
        else:
            print("Incorrecto. Esa letra no está en la palabra.")
            intentos_maximos -= 1
        
        if palabra_adivinada == palabra:
            print("\n¡Felicidades! Has adivinado la palabra:", palabra)
            break
    
    if intentos_maximos == 0:
        print("\n¡Perdiste! La palabra correcta era:", palabra)

# Iniciar el juego
jugar_ahorcado()