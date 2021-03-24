from random import randint
from tkinter import *


window = Tk()
window.title("Rain")
window.resizable(False, False)

width, height = 630, 360
canvas = Canvas(width=width, height=height, bg="#000000", highlightthickness=0)
canvas.pack()

lines = []

while True:

    x, value = randint(0, width), lambda: randint(0, 255)
    lines.append(canvas.create_line(
        x, 0, x, randint(8, 20),
		fill='#%02X%02X%02X' % (value(), value(), value()),
		width=2
    ))
	
    for i in range(len(lines)-58):
        for j in range(len(lines)):
            canvas.move(lines[j], 0, +6)

        canvas.delete(lines[i])
        del(lines[i])
    
    canvas.update()
