import tkinter
from tkinter import *
import random

numOfLines = 20
widthHeight = 700
space = float(float(widthHeight)/float(numOfLines))

window = Tk()
window.resizable(False,False)
mainCanvas = Canvas(width=widthHeight,height=widthHeight)
mainFrame = Frame(width=500,height=100)
mainCanvas.pack()
mainFrame.pack()


for i in range(numOfLines):
    for j in range(numOfLines):
        mainCanvas.create_line(i*space,j*space,(i+1)*space,(j)*space)
        mainCanvas.create_line(i*space,j*space,(i)*space,(j+1)*space)

upButton = Button(mainFrame, text="Up")
upButton.pack()
rightButton = Button(mainFrame, text="Right")
rightButton.pack()
downButton = Button(mainFrame, text="Down")
downButton.pack()
leftButton = Button(mainFrame, text="Left")
leftButton.pack()

window.mainloop()
