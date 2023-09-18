import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea válida.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.delete(seleccion)
    except IndexError:
        messagebox.showwarning("Por favor, selecciona que tarea desea eliminar.")

def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()[0]
        lista_tareas.itemconfig(seleccion, {'bg':'light gray', 'strike':True})
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")
        
def cambiar_color():
    app.configure(bg=color_fondo.get())
    
app = tk.Tk()
app.title("Lista de Tareas")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label_tarea = tk.Label(frame, text="Tarea:")
label_tarea.grid(row=0, column=0)

entrada_tarea = tk.Entry(frame, width=30)
entrada_tarea.grid(row=0, column=1)

boton_agregar = tk.Button(frame, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.grid(row=0, column=2)

boton_marcar_completada = tk.Button(frame, text="Marcar como Completada", command=marcar_completada)
boton_marcar_completada.grid(row=1, column=0, columnspan=3)

boton_eliminar = tk.Button(frame, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=2, column=0, columnspan=3)

lista_tareas = tk.Listbox(frame, selectmode=tk.SINGLE, width=40, height=10)
lista_tareas.grid(row=3, column=0, columnspan=3)

color_fondo = tk.StringVar()
color_boton = tk.StringVar()

color_fondo.set("white")
color_boton.set("lightgray")

label_color_fondo = tk.Label(app, text="Color de fondo de la ventana principal:")
entry_color_fondo = tk.Entry(app, textvariable=color_fondo)

boton_cambiar = tk.Button(app, text="Cambiar Colores", command=cambiar_color)

label_color_fondo.pack()
entry_color_fondo.pack()

boton_cambiar.pack()

app.mainloop()