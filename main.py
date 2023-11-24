import tkinter as tk
import time
from tkinter import ttk
from tkinter import PhotoImage
def cargar_imagen(ruta):
    return tk.PhotoImage(file=ruta)

# Función para cambiar la imagen de fondo de la pestaña
def cambiar_fondo_pestaña(pestana, imagen):
    fondo = tk.Label(pestana, image=imagen)
    fondo.place(relwidth=1, relheight=1)
    pestana.image = imagen  # Para evitar que el recolector de basura elimine la imagen

def actualizar_hora():
    hora_actual = time.strftime('%H:%M:%S')
    hora_decimal.config(text="Hora (Decimal): " + hora_actual)

    hora_entera = int(time.strftime('%H'))
    minuto_entero = int(time.strftime('%M'))
    segundo_entero = int(time.strftime('%S'))

    hora_binaria = f"{decimal_a_binario(hora_entera)}:{decimal_a_binario(minuto_entero)}:{decimal_a_binario(segundo_entero)}"
    hora_base2.config(text="Hora (Binario): " + hora_binaria)

    hora_hexadecimal = f"{decimal_a_hexadecimal(hora_entera)}:{decimal_a_hexadecimal(minuto_entero)}:{decimal_a_hexadecimal(segundo_entero)}"
    hora_base16.config(text="Hora (Hexadecimal): " + hora_hexadecimal)

    if not modificacion_activa:
        root.after(1000, actualizar_hora)

def decimal_a_binario(decimal):
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def decimal_a_hexadecimal(decimal):
    hex_map = "0123456789ABCDEF"
    hexadecimal = ''
    while decimal > 0:
        hexadecimal = hex_map[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal

def modificar_hora():
    try:
        binario = entrada.get()
        unidades = unidades_combo.get()
        global modificacion_activa
        modificacion_activa = True

        if unidades == "Horas":
            operando = int(binario, 2) * 3600
        elif unidades == "Minutos":
            operando = int(binario, 2) * 60
        elif unidades == "Segundos":
            operando = int(binario, 2)

        hora_actual = time.localtime()
        nueva_hora = time.localtime(time.mktime(hora_actual) + operando)
        hora = f"{nueva_hora.tm_hour:02}:{nueva_hora.tm_min:02}:{nueva_hora.tm_sec:02}"
        hora_label.config(text=hora)

        root.after(100, actualizar_hora)  # Esperar 100 ms y luego reanudar la actualización
    except ValueError:
        hora_label.config(text="Error")

root = tk.Tk()
root.title("Proyecto de Modificación de Hora")
root.geometry("500x500")  # Dimensiones fijas
root.resizable(False, False)  # Bloquear la capacidad de maximizar

# Fondo de Aplicacion:


# Crear una interfaz de pestañas
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Pestaña para la Parte 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Parte 1")
imagen1 = cargar_imagen("D:\Descargas\Timer.png")
cambiar_fondo_pestaña(tab1, imagen1)

hora_decimal = tk.Label(tab1, text="", font=("Arial", 16))
hora_base2 = tk.Label(tab1, text="", font=("Arial", 16))
hora_base16 = tk.Label(tab1, text="", font=("Arial", 16))

hora_decimal.pack()
hora_base2.pack()
hora_base16.pack()

# Centrar y agregar espacio entre los labels en la Pestaña 1
for label in [hora_decimal, hora_base2, hora_base16]:
    label.pack_configure(padx=50, pady=50)
    label.pack()

# Pestaña para la Parte 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Parte 2")
cambiar_fondo_pestaña(tab2, imagen1)

hora_label = tk.Label(tab2, text="00:00:00", font=("Arial", 16))
hora_label.pack(pady=20)  # Espaciado vertical

entrada_label = tk.Label(tab2, text="Número binario de 8 bits:")
entrada = tk.Entry(tab2, width=20)
entrada_label.pack(pady=20)  # Espaciado vertical
entrada.pack(pady=20)       # Espaciado vertical

unidades_combo = ttk.Combobox(tab2, values=["Horas", "Minutos", "Segundos"])
unidades_combo.set("Horas")
unidades_combo.pack(pady=20)  # Espaciado vertical

modificar_button = tk.Button(tab2, text="Modificar Hora", command=modificar_hora,width=15, height=2)
modificar_button.pack(pady=20)  # Espaciado vertical


entrada_label.pack()
hora_label.pack()
entrada.pack()
unidades_combo.pack()
modificar_button.pack()

# Variables
modificacion_activa = False

# Iniciar la actualización de hora en tiempo "real" en la Pestaña 2
actualizar_hora()

root.mainloop()