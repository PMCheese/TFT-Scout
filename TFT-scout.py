import pygame
import win32api
import win32con
import win32gui

import tkinter as tk

dead = 0


def startPage():

    frame = tk.Frame(root)

    player1 = tk.StringVar()

    tk.Label(frame, text='player 1').grid(row = 0, column = 0)
    player1entry = tk.Entry(frame, textvariable=player1).grid(row = 0, column = 1)

    player2 = tk.StringVar()

    tk.Label(frame, text='player 2').grid(row = 1, column = 0)
    player2entry = tk.Entry(frame, textvariable=player2).grid(row = 1, column = 1)

    player3 = tk.StringVar()

    tk.Label(frame, text='player 3').grid(row = 2, column = 0)
    player3entry = tk.Entry(frame, textvariable=player3).grid(row = 2, column = 1)

    player4 = tk.StringVar()

    tk.Label(frame, text='player 4').grid(row = 3, column = 0)
    player4entry = tk.Entry(frame, textvariable=player4).grid(row = 3, column = 1)

    player5 = tk.StringVar()

    tk.Label(frame, text='player 5').grid(row = 0, column = 2)
    player1entry = tk.Entry(frame, textvariable=player5).grid(row = 0, column = 3)

    player6 = tk.StringVar()

    tk.Label(frame, text='player 6').grid(row = 1, column = 2)
    player6entry = tk.Entry(frame, textvariable=player6).grid(row = 1, column = 3)

    player7 = tk.StringVar()

    tk.Label(frame, text='player 7').grid(row = 2, column = 2)
    player7entry = tk.Entry(frame, textvariable=player7).grid(row = 2, column = 3)

    startButton = tk.Button(frame, text ="start", command =lambda: startGame(player1.get(), player2.get(), player3.get(), player4.get(), player5.get(), player6.get(), player7.get())).grid(row = 5, column = 0)
    
    return frame



def startGame(p1, p2, p3, p4, p5, p6, p7):

    players = [p1, p2, p3, p4, p5, p6, p7]

    startFrame.destroy()

    p1button = tk.Button(root, text = p1, width = 20, height = 2, bg = 'green', fg = 'white')
    p1button.grid(row = 0, column = 0)
    p2button = tk.Button(root, text = p2, width = 20, height = 2, bg = 'green', fg = 'white')
    p2button.grid(row = 1, column = 0)
    p3button = tk.Button(root, text = p3, width = 20, height = 2, bg = 'green', fg = 'white')
    p3button.grid(row = 2, column = 0)
    p4button = tk.Button(root, text = p4, width = 20, height = 2, bg = 'green', fg = 'white')
    p4button.grid(row = 3, column = 0)
    p5button = tk.Button(root, text = p5, width = 20, height = 2, bg = 'green', fg = 'white')
    p5button.grid(row = 0, column = 3)
    p6button = tk.Button(root, text = p6, width = 20, height = 2, bg = 'green', fg = 'white')
    p6button.grid(row = 1, column = 3)
    p7button = tk.Button(root, text = p7, width = 20, height = 2, bg = 'green', fg = 'white')
    p7button.grid(row = 2, column = 3)
    ghostbutton = tk.Button(root, text = 'GHOST', width = 20, height = 2, bg = 'blue', fg = 'white')
    ghostbutton.grid(row = 3, column = 3)

    buttons = [p1button, p2button, p3button, p4button, p5button, p6button, p7button]

    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 0)).grid(row = 0, column = 2)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 1)).grid(row = 1, column = 2)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 2)).grid(row = 2, column = 2)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 3)).grid(row = 3, column = 2)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 4)).grid(row = 0, column = 4)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 5)).grid(row = 1, column = 4)
    tk.Button(root, text = 'DIE', width = 5, height = 2, command =lambda: updateDead(buttons, 6)).grid(row = 2, column = 4)


    
    p1button.configure(command =lambda: updateButtons(buttons, 0))
    p2button.configure(command =lambda: updateButtons(buttons, 1))
    p3button.configure(command =lambda: updateButtons(buttons, 2))
    p4button.configure(command =lambda: updateButtons(buttons, 3))
    p5button.configure(command =lambda: updateButtons(buttons, 4))
    p6button.configure(command =lambda: updateButtons(buttons, 5))
    p7button.configure(command =lambda: updateButtons(buttons, 6))
    ghostbutton.configure(command =lambda: updatetheStack(buttons))




thestack = [0, 0, 0, 0, 0, 0, 0]

def updateDead(buttons, player):

    global dead

    dead = dead + 1
    buttons[player].configure(bg = 'black')
    doNothing(player)
    buttons[player].configure(command =lambda: doNothing(player))

def doNothing(player):
    thestack[player] = -1

def updatetheStack(buttons):

    for x in range(len(thestack)):
        if thestack[x] > 0: 
            thestack[x] = thestack[x] - 1
        if thestack[x] == 0: 
            buttons[x].configure(bg = 'green')

def updateButtons(buttons, pressed):
    
    print('numdead ')
    print(dead)
    updatetheStack(buttons)
    ## -1 from everyone's timer, unless it's already 0
    
    
    ## set the person you just clicked to maximum timer
    timer = 4-dead
    
    if thestack[pressed] >= 0: 
        buttons[pressed].configure(bg = 'red')
        thestack[pressed] = timer

    print(thestack)

    


    





root = tk.Tk()
root.wm_attributes("-topmost", 1)
root.overrideredirect(1)
root.geometry("400x200")

startFrame = startPage()
startFrame.pack()

root.mainloop()


