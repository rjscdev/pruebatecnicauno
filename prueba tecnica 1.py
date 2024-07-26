import tkinter as tk 
from tkinter import messagebox, ttk

def mostrarmensaje():
    numero = entry.get()
    if numero == "5":
        messagebox.showinfo("test", "prueba aprobada")
    else:
        messagebox.showerror("test", "dato no coincide")

root = tk.Tk()
root.title("Prueba tecnica")
root.geometry("400x300")

etiqueta = tk.Label(root, text="ingrese un numero")
etiqueta.pack(pady = 5)
entry = tk.Entry(root)
entry.pack(pady = 5)
boton = tk.Button(root, text="ejecutar", command=mostrarmensaje)
boton.pack(pady = 5)
root.mainloop()