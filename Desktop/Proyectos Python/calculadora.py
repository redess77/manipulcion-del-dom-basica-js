import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    else:
        return math.sqrt(a)

print("Calculadora en Python")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Raíz cuadrada")
print("7. Salir")

while True:
    opcion = input("Selecciona una operación (1/2/3/4/5/6/7): ")

    if opcion == '7':
        print("¡Hasta luego!")
        break

    if opcion in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Ingresa el primer número: "))
        
        if opcion != '6':
            num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
        elif opcion == '5':
            print("Resultado:", potencia(num1, num2))
        elif opcion == '6':
            print("Resultado:", raiz_cuadrada(num1))
    else:
        print("Opción no válida")