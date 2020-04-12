from tkinter import *
from my_coinbase import *
import time

ventana = Tk()
ventana.geometry('400x200')
ventana.title("PyCoinbase")
def actualizar_datos():
	lbl = Label(ventana, text=cambio_actual(), font=("Arial Bold", 40))
	lbl.grid(column=10, row=10)
	lb2 = Label(ventana, text=mi_cartera(), font=("Arial Bold", 40))
	lb2.grid(column=10, row=80)

actualizar_datos()

while True:
  # Actualiza cada minuto. Más exáctamente en el segundo 5 de cada minuto.
	if time.localtime()[5] == 5:
		actualizar_datos()
	ventana.update_idletasks()
	ventana.update()
	
