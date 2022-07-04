# En este ejercicio teneis que crear una lista de RadioButton que muestre la opcion que se ha
# seleccionado y que contenga un botón de reinicio para que dejetodo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk


def select():
    monitor.config(text="You selected: {}".format(option.get()))


def reset():
    option.set("None")
    monitor.config(text="")


# Ventana
window = tkinter.Tk()
window.title("Install new update?")
window.config(bg="white")
window.geometry("300x130")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)  # Evita que podamos cambiar el tamaño de la ventana


option = tkinter.StringVar()

# Opciones de radiobutton
response_1 = ttk.Radiobutton(window, text="Yes", variable=option, value="Yes", command=select)
response_2 = ttk.Radiobutton(window, text="No", variable=option, value="No", command=select)
response_3 = ttk.Radiobutton(window, text="Remindme later", variable=option, value="Remindme later", command=select)

response_1.grid(column=0, row=1, sticky="WE", pady=2, padx=1)
response_2.grid(column=0, row=2, sticky="WE", pady=2, padx=1)
response_3.grid(column=0, row=3, sticky="WE", pady=2, padx=1)

# Boton de reinicio
restart_button = ttk.Button(window, text="Restart", command=reset)
restart_button.grid(column=0, row=4, sticky="WE", pady=2, padx=1)

# Respuesta seleccionada
monitor = tkinter.Label(window)
monitor.grid(column=0, row=5, sticky="WE", pady=2, padx=2)


window.mainloop()
