from tkinter import

#
#
#

BASE = 460
ALTURA = 220 

#
#
#
ventana_principal = Tk()
ventana_principal.title("Grafica 2d")
ventana_principal.resizable(False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg = "white")

#
#Frame de graficacion 
#
frame_graficacion = Frame(ventana_principal)
frame_graficacion.congif(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

#
# Lienzo de graficacion
#
c = Canvas(frame_graficacion,width=BASE, height=ALTURA)
C.config(bg= "black")
c.place(x=10,y=10)

#
#lineas rectas
#
linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0, fill="red", width=2)
linea_2 = c.create_line(0,0, BASE/2, ALTURA/2, BASE, 0, fill="red", width=2)

#
# Dibujar texto
#
texto_1 = c.create_text(BASE/4,ALTURA/4,anchor="center", text="Daniel Andres", font = ("Arial", 25, "bold"), fill= "blue", activefill="yellow")

#
# Rectangulo
#
rectangulo_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE, 0, fill="pink", outline="blue" )

#
# Poligono
#

Poligono_1 = c.create_polygon(0,0, BASE/2, ALTURA/2, ALTURA,fill="red", outline= "red" )

#
# Circulos
#

circulo_1 = c.create_oval(BASE/2-50, ALTURA/2-50, BASE/2+50, ALTURA/2+50 fill= "orange" outline = "green")

#
# Arcos
#
arco_1 = c.create_arc(BASE/2-30, ALTURA/2-30, BASE/2+30, ALTURA/2+30, start = 30, extent = 300, fill = "black")

#
#Frame de controles
#
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=
frame_graficacion

#
#
#

ventana_principal.mainloop()