#!/usr/bin/env python
import game_engine as g
import game_structure as structure
from pynput.keyboard import Key, Listener
from game_display import*
import threading
import copy
import time
import random
import game_MapSaver as MS

g.player.spawn('▲')
MName = g.mob.spawn()

#places structures
def place_struct(x, y, size):
    struct = structure.geometry.Square(size, x, y)
    g.Game.structures.append((struct[1], struct[2]))
    print((struct[1], struct[2]))
    for i in struct[0]:
        g.blocs.place(i[0], i[1], g.Item.Obstacle)
#
struct = structure.structure.Castle(g.Game.maxMap, g.Game.Map)
g.Game.structures.append((struct[1], struct[2]))
print((struct[1], struct[2]))
for i in struct[0]:
    g.blocs.place(i[0], i[1], g.Item.Obstacle)

place_struct(21, 21, 5)

#pop some x obstacles 

g.blocs.pop(1000)

keys = {Key.ctrl:0}
def on_press(key):
    keys[key] = 1
    name = g.Game.player
    if key == Key.right:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'right')
        else:
            g.player.oldX = g.Game.lives[g.Game.player][1]
            g.player.oldY = g.Game.lives[g.Game.player][2]
            g.player.move_right(name)
        
    elif key == Key.left:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'left')
        else:
            g.player.oldX = g.Game.lives[g.Game.player][1]
            g.player.oldY = g.Game.lives[g.Game.player][2]
            g.player.move_left(name)
            
    elif key == Key.up:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'up')
        else:
            g.player.oldX = g.Game.lives[g.Game.player][1]
            g.player.oldY = g.Game.lives[g.Game.player][2]
            g.player.move_up(name)
            
    elif key == Key.down:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'down')
        else:
            g.player.oldX = g.Game.lives[g.Game.player][1]
            g.player.oldY = g.Game.lives[g.Game.player][2]
            g.player.move_down(name)
            
    elif key == Key.enter:
        if keys[Key.ctrl] == 1:
            All = MS.reuse()
            g.Game.Map = All[0]
            g.Game.lives = All[1]
            g.Game.obstacles = All[2]
            
        else:
            MS.save(g.Game.Map, g.Game.lives, g.Game.obstacles)
    
            
    if key == Key.space:
        g.player.Construct(name)
    if key == Key.backspace:
        g.player.Break(name)
    
        

def on_release(key):
    keys[key] = 0
    if key == Key.esc:
        
        return False

def findRealGoodMap():
    map = g.Game.Map
    realMap = []
    perso = g.Game.lives[g.Game.player]
    Max = g.Game.maxMap
    
    if perso[2]-5 <= 0:
        if perso[1]+5 >= Max:
            for i in range(-5,0):
                realMap.append(map[perso[1] + i] [0 : 10])
            for i in range(5):
                realMap.append(map[(i+perso[1])%100] [0 : 10])
        else:
            for i in range(-5,5):
                realMap.append(map[perso[1] + i] [0 : 10])
        
    elif perso[2]+5 >= Max:
        if perso[1]+5 >= Max:
            for i in range(-5,0):
                realMap.append(map[perso[1] + i] [Max-10 : Max])
            for i in range(5):
                realMap.append(map[(i+perso[1])%100] [Max-10 : Max])
        else:
            for i in range(-5,5):
                realMap.append(map[perso[1] + i] [Max-10 : Max])
    #trouve pas comment modifier x pour que on puisse allez + loin que END-4 bloc.
    
    elif perso[1]+5 >= Max:
        for i in range(-5,0):
            realMap.append(map[perso[1] + i] [perso[2]-5 : perso[2]+5])
        for i in range(5):
            realMap.append(map[(i+perso[1])%100] [perso[2]-5 : perso[2]+5])

        
    else:
        for i in range(-5,5):
            realMap.append(map[perso[1] + i] [perso[2]-5 : perso[2]+5])
    
    return realMap


#Here starts Backgrounds Tasks

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()        
            
t = BackgroundTasks()
t.start()        

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        mapp = copy.deepcopy(g.Game.Map)
        lives = g.Game.lives
        while True:
            new = copy.deepcopy(g.Game.Map)
            try:
                newLives = copy.deepcopy(g.Game.lives)
            except RuntimeError:
                pass
            if mapp != new or lives != newLives:
                show(findRealGoodMap(), g.Game.lives[g.Game.player][0],g.Game.player, newLives)
                mapp = copy.deepcopy(new)
                try:
                    lives = copy.deepcopy(newLives)
                except RuntimeError:
                    pass
            
z = BackgroundTasks()
z.start()        