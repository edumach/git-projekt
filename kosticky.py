import tkinter

canvas = tkinter.Canvas()
canvas.pack()


def kostka():
    canvas.create_rectangle(20,20,60,30)

def kostka2():
    canvas.create_rectangle(50,50,50,50)

kostka()
kostka2()

canvas.mainloop()