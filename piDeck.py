# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:19:25 2020

@author: Bri
"""

import sys
import time
import random as ran
import pyglet
from pyglet.window import mouse
import resources

nButtonsX = 4
nButtonsY = 2

display = pyglet.canvas.get_display()
screens = display.get_screens()
window = pyglet.window.Window(fullscreen=True,screen=screens[1])

# winX = 100
# winY = 100
# window = pyglet.window.Window(winX,winY)

buttons = []
for i in range(nButtonsX*nButtonsY):
    buttons.append(pyglet.sprite.Sprite(resources.square))
    buttons[i].scale = 0.2*window.height/buttons[i].height


def main():
    setup()
    pyglet.app.run()
    return

def setup():
    spacingY = window.height/nButtonsY-buttons[0].height
    spacingX = window.width/nButtonsX-buttons[0].width
    # button[0].x = spacingX
    n=0
    for i in range(nButtonsY):
        for j in range(nButtonsX):
            
            buttons[n].x = spacingX*(n%(nButtonsX))+buttons[n].width*(n%(nButtonsX))+spacingX/2
            # buttons[n].y = spacingY*(n%(nButtonsY))+buttons[n].height*(n%(nButtonsY))+spacingY/2
            if n <= nButtonsX/2+1:
                buttons[n].y = int(spacingY*1)
            else:
                buttons[n].y = int(spacingY*2)
            print(str(buttons[n].y) + " " + str(buttons[n].x))
            n+=1
            
    
@window.event
def on_mouse_release(x,y,button,mod):
    for b in buttons:
        if x<b.x+b.width and x>b.x and y>b.y and y<b.y+b.height:
            if b.color[1] == 255:
                b.color = (255,0,0)
            else:
                b.color = (255,255,255)
            
    return
    
@window.event
def on_draw():
    window.clear()
    for button in buttons:
        button.draw()
    return

if __name__=="__main__":
    main()