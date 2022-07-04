# En este segundo ejercicio, tendreis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que querais.

import tkinter
from tkinter import ttk

# Ventana
window = tkinter.Tk()
window.title("")
window.resizable(False, False)  # Evita que podamos cambiar el tamaño de la ventana
window.configure(bg="black")

# Etiqueta
label = tkinter.Label(window, text="Selecciona las redes sociales que uses:", bg="violet", fg="black")
label.grid(column=0, row=0, padx=2, pady=2)


# Lista de elementos seleccionables
apps_sorted = sorted(["Twitter", "Facebook", "What\'s App", "Instagram", "Tiktok", "BeReal"])
# pueden añadirse al final las redes sociales que se deseen ya que se ordenan alfabeticamente

apps_dictionary = {}
for i in range(0, len(apps_sorted)):  # Crea el diccionario a partir de la lista de apps
    key = apps_sorted[i]
    value = str(i + 1)
    apps_dictionary[key] = value

print(apps_dictionary)


states = []

for (app, valor) in apps_dictionary.items():  # Crea los botones a partir del diccionario de apps
    v = tkinter.StringVar()
    ttk.Checkbutton(window, text=app, variable=v, onvalue=valor, offvalue=0).grid(column=0, row=valor, sticky="WE")
    states.append(v)  # Para poder seleccionar varias apps a la vez

window.mainloop()
