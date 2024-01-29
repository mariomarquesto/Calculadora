from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("350x360")
ventana.resizable(0, 0)
ventana.config(bg="#F4F4F4")

# Imagen calculadora
imagen_calculadora = Image.open("C:/Users/mario/Documents/GitHub/Calculadora/calculadora.png")
nueva_imagen = imagen_calculadora.resize((75, 75))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(ventana, image=render, bg="#F4F4F4")
label_imagen.image = render
label_imagen.pack(pady=5)

def cfloat(numero):
    try:
        result = float(numero)
    except:
        messagebox.showerror("ERROR", "INTRODUCE BIEN LOS DATOS")
        return 0
    return result

def sumar():
    resultado.set(cfloat(numero1.get()) + cfloat(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(cfloat(numero1.get()) - cfloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cfloat(numero1.get()) * cfloat(numero2.get()))
    mostrarResultado()

def dividir():
    if cfloat(numero2.get()) != 0:
        resultado.set(cfloat(numero1.get()) / cfloat(numero2.get()))
        mostrarResultado()
    else:
        messagebox.showerror("ERROR", "No se puede dividir entre cero.")

def mostrarResultado():
    messagebox.showinfo("RESULTADO", f"El resultado de la operación es: {resultado.get()}")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200, bg="#F4F4F4")
marco.config(bd=4, padx=15, pady=15, relief=SOLID)
marco.pack(side=TOP, anchor=CENTER)
# No alterar su posicionamiento
marco.pack_propagate(False)

Label(marco, text="Primer número:", fg="#333", font=("Arial", 10, "bold"), bg="#F4F4F4").pack()
Entry(marco, textvariable=numero1, justify="center", bg="#EFEFEF", bd=3, font=("Arial", 10)).pack()

Label(marco, text="Segundo número:", fg="#333", font=("Arial", 10, "bold"), bg="#F4F4F4").pack()
Entry(marco, textvariable=numero2, justify="center", bg="#EFEFEF", bd=3, font=("Arial", 10)).pack()

Button(marco, text="Sumar", command=sumar, height=1, width=8, bg="#2ECC71", fg="white", font=("Arial", 9, "bold")).pack(side="left", fill=X, padx=1)
Button(marco, text="Restar", command=restar, height=1, width=8, bg="#3498DB", fg="white", font=("Arial", 9, "bold")).pack(side="left", fill=X, padx=1)
Button(marco, text="Multiplicar", command=multiplicar, height=1, width=8, bg="#F39C12", fg="white", font=("Arial", 9, "bold")).pack(side="left", fill=X, padx=1)
Button(marco, text="Dividir", command=dividir, height=1, width=8, bg="#E74C3C", fg="white", font=("Arial", 9, "bold")).pack(side="left", fill=X, padx=1)

Button(ventana, text="Cerrar", command=ventana.quit, height=2, width=10, bg="#E74C3C", fg="white", font=("Arial", 9, "bold")).pack(side=BOTTOM)

ventana.mainloop()
