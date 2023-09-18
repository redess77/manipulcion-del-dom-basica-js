import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    try:
        longitud = int(input("Longitud de la contraseña: "))
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (Sí/No): ").lower() == "si"
        incluir_simbolos = input("¿Incluir símbolos? (Sí/No): ").lower() == "si"

        contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_simbolos)

        print(f"Contraseña generada: {contrasena_generada}")
    except ValueError:
        print("Error: Ingresa una contraseña válida.")