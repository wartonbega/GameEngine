#!/usr/bin/env python
import game_engine as g
import game_structure as structure
from pynput.keyboard import Key, Listener
import threading
import random
import game_MapSaver as MS
import copy

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
struct = structure.structure.Castle(g.Game.maxMap-5, g.Game.Map)
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
            g.player.move_right(name)
        
    elif key == Key.left:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'left')
        else:
            g.player.move_left(name)
            
    elif key == Key.up:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'up')
        else:
            g.player.move_up(name)
            
    elif key == Key.down:
        if keys[Key.ctrl] == 1:
            g.player.turn(name, 'down')
        else:
            g.player.move_down(name)
            
    elif key == Key.enter:
        if keys[Key.ctrl] == 1:
            g.Game = MS.reuse()
            if (g.Game.lives[g.Game.player][0], g.Game.lives[g.Game.player][1]) in g.Game.water:
                g.player.status='InWater'
            else:
                g.player.status=''
            
        else:
            MS.save(g.Game)
    
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
    HightRight = 0
    if perso[2]-5 <= 0:
        if perso[1]+5 >= Max:
            for i in range(-5,0):
                realMap.append(map[perso[1] + i] [0:10])
            for i in range(5):
                realMap.append(map[(i+perso[1])%100] [0:10])
        else:
            for i in range(-5,5):
                realMap.append(map[perso[1] + i] [0 : 10])
                HightRight = g.Game.lives[g.Game.player][1]*-1
        
    elif perso[2]+5 >= Max:

        if perso[1]+5 >= Max:
            for i in range(-5,0):
                realMap.append(map[perso[1] + i] [Max-10:Max])
            for i in range(5):
                realMap.append(map[(i+perso[1])%100] [Max-10:Max])
        else:
            for i in range(-5,5):
                realMap.append(map[perso[1] + i] [Max-10 : Max])
                HightRight = g.Game.lives[g.Game.player][1]-(Max-5)
    
    elif perso[1]+5 >= Max:
        for i in range(-5,0):
            realMap.append(map[perso[1] + i] [perso[2]-5 : perso[2]+5])
        for i in range(5):
            realMap.append(map[(i+perso[1])%100] [perso[2]-5 : perso[2]+5])

        
    else:
        for i in range(-5,5):
            realMap.append(map[perso[1] + i] [perso[2]-5 : perso[2]+5])
    
    return realMap, HightRight


#Here starts Backgrounds Tasks

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()        
            
t = BackgroundTasks()
t.start()        
#################################################################################### Graphic zone and path computing
import tkinter as tk
root = tk.Tk()
root.title('GameEngine 1.1')
can = tk.Canvas(root, width=500, height=550, bg='black')
can.pack()
 
def Inv(event):
    if event.keycode==10:
        g.player.Inventory.selected=1
    elif event.keycode==11:
        g.player.Inventory.selected=2
    elif event.keycode==13:
        g.player.Inventory.selected=3
playerPos = (g.Game.lives[g.Game.player][1], g.Game.lives[g.Game.player][2])
def task():
    global playerPos
    DisEnPl = []
    can.delete("all")
    RealGoodMap = findRealGoodMap()
    Map = RealGoodMap[0]
    High = RealGoodMap[1]
    Iss = can.winfo_width()/10
    x = 0
    y = 0
    water_points = []
    bloc_points = []
    facing = g.Game.playerPointing
    for i in Map:
        for a in i:
            xM = x + (Iss / 2)
            yM = y + (Iss / 2)
            
            if a == []:
                can.create_rectangle(x, y, x+Iss, y+Iss, fill="black")
                can.create_bitmap(50, 50, background='red')
            ###### create water bloc
            if a == g.Item.Water.skin:
                can.create_rectangle(x, y, x+Iss, y+Iss, fill="blue")
                for i in range(4):
                    xa = random.randint(0, 40)+x
                    ya = random.randint(0,45)+y
                    xb = xa+10
                    can.create_line(xa, ya, xb, ya, width=2, fill='black', stipple="gray50")
                b, c = x, y
                
                water_points.append([[(b+i*10, c+toto*10) for i in range(6) if b+i*10 == x or b+i*10 == x+50 or c+toto*10 == y or c+toto*10 == y+50] for toto in range(6) ])

            #########
            elif a == '■':
                bloc_points.append((x,y,x+Iss,y+Iss))
            if a == '◌':
                can.create_rectangle(x, y, x+Iss, y+Iss, fill="red")
                DisEnPl.append((xM,yM))
            
            
            if a in g.Game.allSkin:
                if g.player.status == 'InWater':
                    can.create_rectangle(x, y, x+Iss, y+Iss, fill="blue")
                    b, c = x, y
                    water_points.append([[(b+i*10, c+toto*10) for i in range(6) if b+i*10 == x or b+i*10 == x+50 or c+toto*10 == y or c+toto*10 == y+50] for toto in range(6) ])
                    for i in range(4):
                        xa = random.randint(0, 40)+x
                        ya = random.randint(0,45)+y
                        xb = xa+10
                        can.create_line(xa, ya, xb, ya, width=2, fill='black')
                PlayerSize=Iss/5
                can.create_rectangle(x+PlayerSize, y+PlayerSize, x+Iss-PlayerSize, y+Iss-PlayerSize, fill="yellow")
                
                DisEnPl.append((xM,yM))
                
                if facing == 'left':
                    can.create_line(xM, yM, x+random.randint(0,3), y+random.randint(0,3), width=2, fill='yellow')
                    can.create_line(xM, yM, x+random.randint(0,3), y+Iss+random.randint(0,3), width=2, fill='yellow')
                elif facing == 'right':
                    can.create_line(xM, yM, x+Iss+random.randint(0,3), y+Iss+random.randint(0,3), width=2, fill='yellow')
                    can.create_line(xM, yM, x+Iss+random.randint(0,3), y+random.randint(0,3), width=2, fill='yellow')
                elif facing == 'up':
                    can.create_line(xM, yM, x+Iss+random.randint(0,3), y+random.randint(0,3), width=2, fill='yellow')
                    can.create_line(xM, yM, x+random.randint(0,3), y+random.randint(0,3), width=2, fill='yellow')
                elif facing == 'down':
                    can.create_line(xM, yM, x+random.randint(0,3), y+Iss+random.randint(0,3), width=2, fill='yellow')
                    can.create_line(xM, yM, x+Iss+random.randint(0,3), y+Iss+random.randint(0,3), width=2, fill='yellow')
            x+=Iss
        y+=Iss
        x = 0
    for v in water_points:
        for w in v:
            for f in v:
                for z in f:
                    can.create_oval(z[0]-10+random.randint(0,5), z[1]-10+random.randint(0,5), z[0]+10-random.randint(0,5), z[1]+10-random.randint(0,5),fill='blue', stipple="gray50", outline = '')
    
    
    for v in bloc_points:
        can.create_rectangle(v[0], v[1], v[2], v[3], fill="white")
#    if (g.Game.lives[g.Game.player][1],g.Game.lives[g.Game.player][2]) == playerPos:
#        pass
#    else:
    playerPos = (g.Game.lives[g.Game.player][1],g.Game.lives[g.Game.player][2])
    if len(DisEnPl) == 2:
        path = []
        x0 = int(DisEnPl[0][0])
        y0 = int(DisEnPl[0][1])
        x1 = int(DisEnPl[1][0])
        y1 = int(DisEnPl[1][1])
        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        dx = x1-x0
        dy = y1-y0
        if dx==0:
            pass
        else:  
            a = dy/dx
            b = y0 - a*x0
            def f(x):
                return a*(x-x0)+y0
            for i in range(x0,x1):
                j1 = round(f(i-(1/2)))
                j2 = round(f(i+(1/2)))
                if j1<j2:
                    j1, j2 = j2, j1
                for j in (j1, j2+1):
                    coorX = i - i%50
                    coorY = j - j%50
                    if (coorX, coorY) in path:
                        pass
                    else:
                        path.append((coorX, coorY))
        for i in path:
            X = i[0]
            Y = i[1]
            can.create_rectangle(X, Y, X+Iss, Y+Iss, fill='orange', stipple='gray50') 
        can.create_line(x0, y0, x1, y1, fill='green')
        mobCoor = []
        for i in path:
            cor0 = i[0]//50
            cor1 = i[1]//50
            RightHigh = (g.Game.lives[g.Game.player][1]-5, g.Game.lives[g.Game.player][2]-5)
            mobCoor.append((cor0+RightHigh[0], cor1+RightHigh[1]))
        
        g.deplacement.CoorSet = []
        for i in mobCoor[1:-1]:
            g.deplacement.CoorSet.append(i)
    else:
        g.deplacement.CoorSet = []
            
    ################################
    
    can.create_text(400,525,fill="white",font="Times 14 bold", text=f"player : x = {g.Game.lives[g.Game.player][1]} y = {g.Game.lives[g.Game.player][2]}\n mob : x = {g.Game.lives['MOB'][1]} y = {g.Game.lives['MOB'][2]}")
    x = 0
    
    for i in range(1, len(g.player.Inventory.inventory)+1):
        if i == g.player.Inventory.selected:
            can.create_rectangle(x, y, x+Iss, y+Iss, width=2, fill='grey')
        if g.player.Inventory.inventory[i] == g.Item.Obstacle:
            can.create_rectangle(x+5, y+5, x+Iss-5, y+Iss-5, width=2, fill='white')
        if g.player.Inventory.inventory[i] == g.Item.Water:
            can.create_rectangle(x+5, y+5, x+Iss-5, y+Iss-5, width=2, fill='blue')
        
        x+=Iss

    root.after(1, task)
    
root.bind('<Key>',Inv)
root.after(500, task)
root.mainloop()