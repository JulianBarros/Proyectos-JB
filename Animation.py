import time
from tkinder import *
ventana = Tk()

lienzo = Canvas(ventana, width = 500, height = 500)

lienzo.pack()
lienzo.create_rectangle(10,10,20,20)
time.sleep(5)
