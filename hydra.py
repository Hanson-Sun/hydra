from tkinter import *
import random

wcount = 1

main = Tk()

def hydra():
    global wcount
    wcount = wcount * 2
    window.destroy
    for i in range(0, wcount):
        create()

main.protocol("WM_DELETE_WINDOW",hydra)

size = str(random.randint(400,800)) + "x" + str(random.randint(400,800))
main.geometry(size)

window = main

def create():
    window = Toplevel(main)
    b1 = Button(window, text = "Hydra", width = 50, height = 25, command = hydra)
    b1.pack()
    size = str(random.randint(400,800)) + "x" + str(random.randint(400,800))
    window.geometry(size)
    window.protocol("WM_DELETE_WINDOW",hydra)



b = Button(main, text = "Kill Hydra", width = 50, height = 25, command = create)
b.pack()

mainloop()
