import tkinter
from tkinter import *
import random

numOfLines = 20
widthHeight = 700
space = float(float(widthHeight)/float(numOfLines))

class Snake:

    applePlace = []
    snakeBodyPlace = []

    def __init__(self):
        self.applePlace = [random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)]
        self.snakeBodyPlace.append([random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)])

    def endGame(self):
        pass

    def addBody(self):
        pass

    def addApple(self):
        pass

    def eatApple(self):
        pass

    def addMove(self):
        pass

    def drawEntity(self):
        mainCanvas.delete("all")
        for i in range(numOfLines):
            for j in range(numOfLines):
                mainCanvas.create_line(i*space,j*space,(i+1)*space,(j)*space)
                mainCanvas.create_line(i*space,j*space,(i)*space,(j+1)*space)

        mainCanvas.create_rectangle(self.applePlace[0]*space,self.applePlace[1]*space,
                                    (self.applePlace[0]+1)*space,(self.applePlace[1]+1)*space, fill="#ff0000")

window = Tk()
window.resizable(False,False)
mainCanvas = Canvas(width=widthHeight,height=widthHeight)
mainFrame = Frame(width=500,height=100)
mainCanvas.pack()
mainFrame.pack()

snake = Snake()
snake.drawEntity()


upButton = Button(mainFrame, text="Up")
upButton.pack()
rightButton = Button(mainFrame, text="Right")
rightButton.pack()
downButton = Button(mainFrame, text="Down")
downButton.pack()
leftButton = Button(mainFrame, text="Left")
leftButton.pack()

window.mainloop()
