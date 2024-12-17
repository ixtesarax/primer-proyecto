import tkinter as tk
from tkinter import simpledialog, messagebox

tareas = []


def agregar_tarea():
    tt = simpledialog.askstring("agregar tarea", "titulo de la tarea:")
    
    if tt:
        tareas.append({"titulo": tt, "completada": False})
        actualizar_lista()


def actualizar_lista():
    lista_tareas.delete(0, tk.END)  
    
    for idx, tarea in enumerate(tareas):
        estado = "completada" if tarea["completada"] else "pendiente"
        lista_tareas.insert(tk.END, f"{idx + 1}. {tarea['titulo']} - {estado}")


def marcar_completada():
    seleccion = lista_tareas.curselection()
    
    if seleccion:
        idx = seleccion[0]
        tareas[idx]["completada"] = True
        actualizar_lista()
        
    else:
        messagebox.showwarning("atencion", "debes seleccionar una tarea")


def eliminar_completadas():
    global tareas
    tareas = [tarea for tarea in tareas if not tarea["completada"]]
    actualizar_lista()


v = tk.Tk()
v.title("gestor basico de tareas")


lista_tareas = tk.Listbox(v, width=50, height=10)
lista_tareas.pack(pady=10)


btn_agregar = tk.Button(v, text="agregar tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(v, text="marcar completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(v, text="eliminar completadas", command=eliminar_completadas)
btn_eliminar.pack(pady=5)


v.mainloop()
