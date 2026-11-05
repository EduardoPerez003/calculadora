import tkinter as tk

# Operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

# Funciones de los botones
def sumar():
    resultado.config(text="Resultado: " + str(suma(int(caja1.get()), int(caja2.get()))))

def restar():
    resultado.config(text="Resultado: " + str(resta(int(caja1.get()), int(caja2.get()))))

def multiplicar():
    resultado.config(text="Resultado: " + str(multiplicacion(int(caja1.get()), int(caja2.get()))))

def dividir():
    a = int(caja1.get())
    b = int(caja2.get())
    if b == 0:
        resultado.config(text="No se puede dividir entre 0")
    else:
        resultado.config(text="Resultado: " + str(division(a, b)))

# Ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x350")

tk.Label(ventana, text="Primer numero").pack(pady=5)
caja1 = tk.Entry(ventana)
caja1.pack()

tk.Label(ventana, text="Segundo numero").pack(pady=5)
caja2 = tk.Entry(ventana)
caja2.pack()

# Botones para elegir la operacion
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Button(ventana, text="Restar", command=restar).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=5)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=5)

# Resultado
resultado = tk.Label(ventana, text="Elige una operacion")
resultado.pack(pady=10)

ventana.mainloop()
