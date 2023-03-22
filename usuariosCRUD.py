from tkinter import *
from tkinter import tkk
import tkinter as tk

ventana= tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")
panel= tkk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1=tkk.Frame(panel)
pestana2=tkk.Frame(panel)
pestana3=tkk.Frame(panel)
pestana4=tkk.Frame(panel)


#pestaña1: formulario de registro
titulo=Label(pestana1,text="Registro usuario", fg = "blue",font=("modern",18)).pack()

panel.add(pestana1, text="formulario de usuario")
panel.add(pestana2,text="Buscar usuarios")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Actualizar usuarios")

varNom= tk.StringVar()
lbNom= Label(pestana1,text="nombre:").pack()
txtNom=Entry(pestana1,textevariable=varNom).pack()

varCor= tk.StringVar()
lbCor= Label(pestana1,text="correo:").pack()
txtCor=Entry(pestana1,textevariable=varCor).pack()

varCon= tk.StringVar()
lbCon= Label(pestana1,text="cotraseña:").pack()
txtCon=Entry(pestana1,textevariable=varCon).pack()

btGuardar=Button(pestana1,text="Guardar usuario").pack




ventana.mainloop()