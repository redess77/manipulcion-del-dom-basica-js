import tkinter as tk
import math

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = combo_operacion.get()
        if operacion == 'Suma':
            resultado.set(num1 + num2)
        elif operacion == 'Resta':
            resultado.set(num1 - num2)
        elif operacion == 'Multiplicación':
            resultado.set(num1 * num2)
        elif operacion == 'División':
            if num2 == 0:
                resultado.set("Error: No se puede dividir por cero")
            else:
                resultado.set(num1 / num2)
        elif operacion == 'Potencia':
            resultado.set(num1 ** num2)
        elif operacion == 'Raíz Cuadrada':
            if num1 < 0:
                resultado.set("Error: No se puede calcular la raíz cuadrada de un número negativo")
            else:
                resultado.set(math.sqrt(num1))
    except ValueError:
        resultado.set("Error: Entrada no válida")

app = tk.Tk()
app.title("Calculadora")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label_num1 = tk.Label(frame, text="Número 1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1)

label_operacion = tk.Label(frame, text="Operación:")
label_operacion.grid(row=1, column=0)

operaciones = ['Suma', 'Resta', 'Multiplicación', 'División', 'Potencia', 'Raíz Cuadrada']
combo_operacion = tk.StringVar()
combo_operacion.set(operaciones[0])

combo = tk.OptionMenu(frame, combo_operacion, *operaciones)
combo.grid(row=1, column=1)

label_num2 = tk.Label(frame, text="Número 2:")
label_num2.grid(row=2, column=0)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=2, column=1)

boton_calcular = tk.Button(frame, text="Calcular", command=calcular)
boton_calcular.grid(row=3, columnspan=2)

resultado = tk.StringVar()
label_resultado = tk.Label(frame, textvariable=resultado)
label_resultado.grid(row=4, columnspan=2)

app.mainloop()