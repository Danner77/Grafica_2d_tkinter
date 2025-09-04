from tkinter import *

# ------------------
# variables globales
# ------------------
BASE = 460
ALTURA = 220

# ----------------
# ventana prncipal
# ----------------
ventana_principal = Tk()
ventana_principal.title("graficas 2d")
ventana_principal.resizable(FALSE, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg = "cyan")

# --------------------
# frame de graficacion
# --------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "light gray", width=310, height=150)
frame_graficacion.place(x=90,y=230)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=150, height=120)
frame_graficacion.place(x=250,y=110)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "light gray", width=130, height=100)
frame_graficacion.place(x=260,y=120)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=50, height=150)
frame_graficacion.place(x=30,y=230)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=20, height=120)
frame_graficacion.place(x=70,y=250)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=170, height=20)
frame_graficacion.place(x=240,y=100)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=130, height=20)
frame_graficacion.place(x=260,y=80)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "gray", width=50, height=80)
frame_graficacion.place(x=130,y=150)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg = "black", width=60, height=20)
frame_graficacion.place(x=125,y=150)






# ---------------------------
# desplegar ventana principal
# ---------------------------
ventana_principal.mainloop()