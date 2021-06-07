from tkinter import *
import numpy as np
from math import *
from random import *
import random
import keyboard

tk = Tk()
cnv=Canvas(tk, width=1600, height=900, bg="grey")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales


#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class player(object):
    def __init__(self, name):
        self.name = name
        self.x = 800
        self.y = 450
        self.vy = 10
        self.draw = 0

class point(object):
    def __init__(self):
        self.x = 800
        self.y = 450
        self.v = 0
        self.vx = 0
        self.vy = 0
        self.alpha = 0
        self.color = "white"
        self.draw = 0

player1 = player(0)
player2 = player(1)
player1.x = 1500
player2.x = 100

ball = point()

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw():
    cnv.delete(player1.draw)
    cnv.delete(player2.draw)
    cnv.delete(ball.draw)
    player1.draw = cnv.create_rectangle(player1.x-10, player1.y-75, player1.x+10, player1.y+75, fill="red")
    player2.draw = cnv.create_rectangle(player2.x-10, player2.y-75, player2.x+10, player2.y+75, fill="blue")
    ball.draw = cnv.create_rectangle(ball.x-20, ball.y-20, ball.x+20, ball.y+20, fill=ball.color)
    
#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    if keyboard.is_pressed("space"):
        ball.alpha = random.random()*2*np.pi
        ball.v = 10

    if keyboard.is_pressed("up"):
        player1.y -= player1.vy
    if keyboard.is_pressed("down"):
        player1.y += player1.vy
    
    if keyboard.is_pressed("z"):
        player2.y -= player2.vy
    if keyboard.is_pressed("s"):
        player2.y += player2.vy

#-------------------------------------------------------------------------------------------------------------------------------------------
#brain

def brain():
    ball.vx = ball.v*np.cos(ball.alpha)
    ball.vy = ball.v*np.sin(ball.alpha)
    ball.x += ball.vx
    ball.y += ball.vy

#-------------------------------------------------------------------------------------------------------------------------------------------
#new_checkpoint

def new_checkpoint():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#collision

def collision():
    if(ball.y-20 <= 0 or ball.y+20 >= 900):
        ball.alpha *= -1
        
    if(player1.y-75 <= 0):
        player1.y = 75
        
    if(player1.y+75 >= 900):
        player1.y = 825
        
    if(player2.y-75 <= 0):
        player2.y = 75
        
    if(player2.y+75 >= 900):
        player2.y = 825

    if(ball.x+20 >= player1.x-10 and ball.x-20 <= player1.x+10 and ball.y+20 >= player1.y-75 and ball.y-20 <= player1.y+75):
        ball.alpha = (1-(ball.y-player1.y)/300)*np.pi
        ball.v *= 1.01
        ball.color="red"

    if(ball.x-20 <= player2.x+10 and ball.x+20 >= player2.x-10 and ball.y+20 >= player2.y-75 and ball.y-20 <= player2.y+75):
        ball.alpha = (1-(player2.y-ball.y)/300)*np.pi+np.pi
        ball.v *= 1.01
        ball.color="blue"

    if(ball.x-20 <= 0):
        ball.alpha = 0
        ball.v *= 1.01
        ball.color="blue"

    if(ball.x+20 >= 1600):
        ball.alpha = np.pi
        ball.v *= 1.01
        ball.color="red"

#-------------------------------------------------------------------------------------------------------------------------------------------
#main

def main():
    control()
    brain()
    collision()
    draw()
    tk.after(10, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

main()
tk.mainloop()