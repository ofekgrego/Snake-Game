import tkinter
from tkinter import *
import random

numOfLines = 20
widthHeight = 700
space = float(float(widthHeight)/float(numOfLines))

class Snake:

    snakeBodyPlace = []
    newSnakeBodyPlace = []
    applePlace = []
    lastDirc = 5
    newBody = False

    def __init__(self):
        self.applePlace = [random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)]
        self.snakeBodyPlace.append([random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)])

    def endGame(self):
        self.applePlace = []
        self.snakeBodyPlace = []
        self.applePlace = [random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)]
        self.snakeBodyPlace.append([random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)])
        newSnakeBodyPlace = []
        lastDirc = 5
        newBody = False

    def addBody(self):
        self.newBody = True

    def addApple(self):
        self.applePlace = [random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)]
        while self.applePlace in self.snakeBodyPlace:
                self.applePlace = [random.randint(0,numOfLines-1),random.randint(0,numOfLines-1)]
        self.drawEntity()

    def eatApple(self):
        self.addApple()
        self.addBody()

    def addMove(self, dirc):
        endGame = False
        speMove = False
        if self.newBody:
            self.newBody = False
            self.snakeBodyPlace.append(self.snakeBodyPlace[len(self.snakeBodyPlace)-1])
        if dirc == -1:
            dirc = self.lastDirc
            speMove = True
        for i in range(len(self.snakeBodyPlace)):
            if i == 0:
                if dirc == 0:
                    if self.lastDirc == 2 and len(self.snakeBodyPlace) != 1:
                        self.endGame()
                        endGame = True
                    elif self.snakeBodyPlace[0][1] == 0:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0],numOfLines-1])
                    else:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0],self.snakeBodyPlace[0][1]-1])
                    self.lastDirc = 0

                elif dirc == 1:
                    if self.lastDirc == 3 and len(self.snakeBodyPlace) != 1:
                        self.endGame()
                        endGame = True
                    elif self.snakeBodyPlace[0][0] == numOfLines-1:
                        self.newSnakeBodyPlace.append([0,self.snakeBodyPlace[0][1]])
                    else:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0]+1,self.snakeBodyPlace[0][1]])
                    self.lastDirc = 1

                elif dirc == 2:
                    if self.lastDirc == 0 and len(self.snakeBodyPlace) != 1:
                        self.endGame()
                        endGame = True
                    elif self.snakeBodyPlace[0][1] == numOfLines-1:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0],0])
                    else:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0],self.snakeBodyPlace[0][1]+1])
                    self.lastDirc = 2

                else:
                    if self.lastDirc == 1 and len(self.snakeBodyPlace) != 1:
                        self.endGame()
                        endGame = True
                    elif self.snakeBodyPlace[0][0] == 0:
                        self.newSnakeBodyPlace.append([numOfLines-1,self.snakeBodyPlace[0][1]])
                    else:
                        self.newSnakeBodyPlace.append([self.snakeBodyPlace[0][0]-1,self.snakeBodyPlace[0][1]])
                    self.lastDirc = 3

                # seen = []
                # print(self.newSnakeBodyPlace)
                # for number in self.snakeBodyPlace:
                #     if number in seen:
                #         self.endGame()
                #         endGame = True
                #     else:
                #         seen.append(number)

                if endGame != True and self.newSnakeBodyPlace[0] == self.applePlace:
                    self.eatApple()
            elif endGame != True:
                self.newSnakeBodyPlace.append(self.snakeBodyPlace[i-1])

        if endGame != True:
            self.snakeBodyPlace = self.newSnakeBodyPlace
            self.newSnakeBodyPlace = []

            self.drawEntity()
        if speMove:
            window.after(1000, lambda Zero=10: snake.addMove(-1))

    def drawEntity(self):
        mainCanvas.delete("all")
        for i in range(numOfLines):
            for j in range(numOfLines):
                mainCanvas.create_line(i*space,j*space,(i+1)*space,(j)*space)
                mainCanvas.create_line(i*space,j*space,(i)*space,(j+1)*space)
        for i in range(len(self.snakeBodyPlace)):
            body = self.snakeBodyPlace[i]
            mainCanvas.create_rectangle(body[0]*space,body[1]*space,
                                        (body[0]+1)*space,(body[1]+1)*space, fill="#" + str(i%10) + str(i%10) + str(i%10))

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


upButton = Button(mainFrame, text="Up", command=lambda Zero=0: snake.addMove(0))
upButton.pack()
rightButton = Button(mainFrame, text="Right", command=lambda Zero=1: snake.addMove(1))
rightButton.pack()
downButton = Button(mainFrame, text="Down", command=lambda Zero=2: snake.addMove(2))
downButton.pack()
leftButton = Button(mainFrame, text="Left", command=lambda Zero=3: snake.addMove(3))
leftButton.pack()

window.after(1000, lambda Zero=10: snake.addMove(-1))
window.mainloop()
