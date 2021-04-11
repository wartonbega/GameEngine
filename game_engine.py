import threading
import random
import time

class Game:
    def __main__():
        Map = [[[ ]for i in range(100)] for x in range(100)]
        return Map
    #lives{name : (life, x, y, damage average) }
    lives = {}
    maxMap = 100
    player = ''
    allSkin = ['▶','◀','▲','▼']
    playerSkin = '▲'
    playerPointing = 'up'
    obstacles = []
    water = []
    structures = []

    #Map[x][y]
    Map = __main__()

class deplacement:
    CoorSet = []
    def goto(x, y, xb, yb):
        xRet = x
        yRet = y
        if x < xb and not player.GoInObs(x+1,y):
            deplacement.OT=0
            xRet+=1
        elif x > xb and not player.GoInObs(x-1,y):
            xRet-=1
            deplacement.OT=0
        elif y < yb and not player.GoInObs(x,y+1):
            deplacement.OT=1
            yRet+=1
        elif y > yb and not player.GoInObs(x,y-1):
            deplacement.OT=1
            yRet-=1
        return (xRet, yRet)
    
class Fight:        
    def WhoIsInNineByNine(name):
        livings = []
        AllLivesKey = Game.lives.keys()
        x = Game.lives[name][1]
        y = Game.lives[name][2]
        
        for i in AllLivesKey:
            xl = Game.lives[i][1]
            yl = Game.lives[i][2]
            if i == name:
                pass
            else:
                if abs(x-xl)<=1 and abs(y-yl)<=1 and not (x==xl and y==yl):
                    livings.append(i)
        return livings
    
    def TakesDammage(name, hit):
        Game.lives[name] = (Game.lives[name][0]-hit, Game.lives[name][1], Game.lives[name][2], Game.lives[name][3])
    
    #            x
    #attack :   xOx
    #            x
    def Attack(name):
        ennemies = Fight.WhoIsInNineByNine(name)
        dammage = Game.lives[name][3]
        for i in ennemies:
            Fight.TakesDammage(i, dammage)
        return

    
#obstacles are uncrossable and are summoned randomly.
class blocs:
    def IsInStruct(x,y):
        for i in Game.structures:
            if i[0][0] <= x <= i[1][0] and i[0][1] <= y <= i[1][1]:
                return True
        
    def pop(quantity):
        for i in range(quantity):
            x = random.randint(0,99)
            y = random.randint(0,99)
            if blocs.IsInStruct(x,y):
                pass
            else:
                if (x,y) in Game.obstacles:
                    pass
                else:
                    if x == 20 and y == 20:
                        x+=1
                    Game.Map[x][y] = Item.Obstacle.skin
                    Game.obstacles.append((x,y))
            
    def place(x, y, type):
        if type == Item.Obstacle:
            
            if (x,y) in Game.obstacles:
                return
            else:
                if x == 20 and y == 20:
                    x+=1
                if (x, y) in Game.water:
                    blocs.remove(x, y)
                
                Game.Map[x][y] = Item.Obstacle.skin
                Game.obstacles.append((x,y))
        
        elif type == Item.Water:
            if (x,y) in Game.water:
                return
            else:
                if (x, y) in Game.obstacles:
                    return
                Game.Map[x][y] = Item.Water.skin
                Game.water.append((x,y))
            
    def remove(x, y):
        if (x, y) in Game.obstacles:
            i = 0
            for w in Game.obstacles:
                i+=1
                if w == (x, y):
                    Game.obstacles.remove(w)
                    Game.Map[x][y]=[]
                    break
                
        if (x, y) in Game.water:
            i = 0
            for w in Game.water:
                i+=1
                if w == (x, y):
                    Game.water.remove(w)
                    Game.Map[x][y]=[]
                    break
        else:
            return
    

class bonus:
    class heart:
        def PassOnWhile(x, y, effect = None, *oui):
            class BackgroundTasks(threading.Thread):
                def run(self,*args,**kwargs):
                    while True:
                        xPlayer = Game.lives[Game.player][1]
                        yPlayer = Game.lives[Game.player][2]
                        if x == xPlayer and y == yPlayer:
                            player.gainLife(5)
                            print(*oui)
                            if effect:
                                effect(*oui)
                            break
                            
            z = BackgroundTasks()
            z.start()
            
        def pop(effect = None, *args):
            x = random.randint(0,9)
            y = random.randint(0,9)
            if (x,y) in Game.obstacles:
                bonus.pop(effect, args)
            else:
                Game.Map[x][y] = '♡'
                bonus.heart.PassOnWhile(x,y, effect, *args)

class Item(object):
    class Obstacle:
        skin = '■'
    class Water:
        skin = '▤'
        
        def InWater(name):
            x = Game.lives[Game.player][1]
            y = Game.lives[Game.player][2]
            player.Time1 = time.time()
            if (x, y) in Game.water:
                return True
        def GoesOutOfWater(xold, yold):
            if (xold, yold) in Game.water:
                Game.Map[xold][yold] = Item.Water.skin
                player.status = 'OutOfWater'
                
    
#only one player can be played
#the map is limitless, when you arrive to a boarder, you get teleported to the other side
class player:
    oldX = 0
    oldy = 0
    status = ''
    class Inventory:
        inventory = {1:Item.Obstacle, 2:Item.Water}
        selected = 2
        def select(nbr):
            player.Inventory.select = nbr
        
    def Construct(name):
        pointing = Game.playerPointing
        Px = Game.lives[name][1]
        Py = Game.lives[name][2]
        if pointing == 'up':
            x, y = Px-1, Py
        elif pointing == 'down':
            x, y = Px+1, Py
        elif pointing == 'left':
            x, y = Px, Py-1
        elif pointing == 'right':
            x, y = Px, Py+1
        
        blocs.place(x, y, player.Inventory.inventory[player.Inventory.selected])

    def Break(name):
        pointing = Game.playerPointing
        Px = Game.lives[name][1]
        Py = Game.lives[name][2]
        if pointing == 'up':
            x, y = Px-1, Py
        elif pointing == 'down':
            x, y = Px+1, Py
        elif pointing == 'left':
            x, y = Px, Py-1
        elif pointing == 'right':
            x, y = Px, Py+1
        blocs.remove(x, y)
    
    def spawn(name, life = 10 , x = 20, y = 20, DammageAverage = 2):
       Game.lives[name] = (life, x, y, DammageAverage)
       Game.Map[x][y] = Game.playerSkin
       Game.player = name
    
    def FocusOn(name):
        Game.player = name
    
    def GoInObs(x,y):
        livingsCoord = []
        for i in Game.lives:
            livingsCoord.append((Game.lives[i][1],Game.lives[i][2]))
        if (x,y) in Game.obstacles:
            return True
        elif (x,y) in livingsCoord:
            return True
        else:
            return False
    
    def turn(name, side):
        Game.playerPointing = side
        if side == 'left':
            Game.Map[Game.lives[Game.player][1]][Game.lives[Game.player][2]] = Game.allSkin[1]
        elif side == 'right':
            Game.Map[Game.lives[Game.player][1]][Game.lives[Game.player][2]] = Game.allSkin[0]
        elif side == 'up':
            Game.Map[Game.lives[Game.player][1]][Game.lives[Game.player][2]] = Game.allSkin[2]
        elif side == 'down':
            Game.Map[Game.lives[Game.player][1]][Game.lives[Game.player][2]] = Game.allSkin[3]
    Time1 = 0
    Time2 = 0
    
    def MoveFunction(playerName, x, y, xOld, yOld):
        if not player.GoInObs(x,y):
            if player.status == 'InWater':
                player.Time2 = time.time()
                if player.Time2 - player.Time1 < 0.5:
                    return
            Game.Map[x][y], Game.Map[xOld][yOld] = Game.playerSkin, [] 
            Game.lives[playerName]= (Game.lives[playerName][0], x, y, Game.lives[playerName][3])
            Item.Water.GoesOutOfWater(xOld, yOld)
            if Item.Water.InWater(playerName):
                player.status = 'InWater'
            
        else:
            Game.Map[xOld][yOld] = Game.playerSkin
    
    def move_right(playerName):
        x = (Game.lives[playerName][1])%100
        y = (Game.lives[playerName][2]+1)%100
        xOld = Game.lives[playerName][1]
        yOld = Game.lives[playerName][2]
        Game.playerPointing = 'right'
        Game.playerSkin = Game.allSkin[0]
        player.MoveFunction(playerName, x, y , xOld, yOld)
        
            
        
    def move_left(playerName):
        x = (Game.lives[playerName][1])%100
        y = (Game.lives[playerName][2]-1)%100
        xOld = Game.lives[playerName][1]
        yOld = Game.lives[playerName][2]
        Game.playerPointing = 'left'
        Game.playerSkin = Game.allSkin[1]
        player.MoveFunction(playerName, x, y , xOld, yOld)
        
    def move_down(playerName):
        x = (Game.lives[playerName][1]+1)%100
        y = (Game.lives[playerName][2])%100
        xOld = Game.lives[playerName][1]
        yOld = Game.lives[playerName][2]
        Game.playerPointing = 'down'
        Game.playerSkin = Game.allSkin[3]
        player.MoveFunction(playerName, x, y , xOld, yOld)
            
    def move_up(playerName):
        x = (Game.lives[playerName][1]-1)%100
        y = (Game.lives[playerName][2])%100
        xOld = Game.lives[playerName][1]
        yOld = Game.lives[playerName][2]
        Game.playerPointing = 'up'
        Game.playerSkin = Game.allSkin[2]
        player.MoveFunction(playerName, x, y , xOld, yOld)
    
    def gainLife(life):
        Game.lives[Game.player] = (Game.lives[Game.player][0]+life, Game.lives[Game.player][1], Game.lives[Game.player][2], Game.lives[Game.player][3])


class mob:
    life = 5
    def Break(x,y):
        if (x,y) in Game.obstacles:
            blocs.remove(x, y)
        
    def up(name):
        x = (Game.lives[name][1]-1)%100
        y = (Game.lives[name][2])%100
        xOld = Game.lives[name][1]
        yOld = Game.lives[name][2]
        if not player.GoInObs(x,y):
            Game.Map[x][y], Game.Map[xOld][yOld] = '◌', [] 
            Game.lives[name]= (Game.lives[name][0], x, y, Game.lives[name][3])
        
    def down(name):
        x = (Game.lives[name][1]+1)%100
        y = (Game.lives[name][2])%100
        xOld = Game.lives[name][1]
        yOld = Game.lives[name][2]
        if not player.GoInObs(x,y):
            Game.Map[x][y], Game.Map[xOld][yOld] = '◌', [] 
            Game.lives[name]= (Game.lives[name][0], x, y, Game.lives[name][3])
    
    def left(name):
        x = (Game.lives[name][1])%100
        y = (Game.lives[name][2]-1)%100
        xOld = Game.lives[name][1]
        yOld = Game.lives[name][2]
        if not player.GoInObs(x,y):
            Game.Map[x][y], Game.Map[xOld][yOld] = '◌', [] 
            Game.lives[name]= (Game.lives[name][0], x, y, Game.lives[name][3])
        
    def right(name):
        x = (Game.lives[name][1])%100
        y = (Game.lives[name][2]+1)%100
        xOld = Game.lives[name][1]
        yOld = Game.lives[name][2]
        if not player.GoInObs(x,y):
            Game.Map[x][y], Game.Map[xOld][yOld] = '◌', [] 
            Game.lives[name]= (Game.lives[name][0], x, y, Game.lives[name][3])
    
    def goto(x, y, name):
        x = x%100
        y = y%100
        xOld = Game.lives[name][1]
        yOld = Game.lives[name][2]
        if not player.GoInObs(x,y):
            Game.Map[x][y], Game.Map[xOld][yOld] = '◌', [] 
            Game.lives[name]= (Game.lives[name][0], x, y, Game.lives[name][3])
        
    def depop(name):
        x = (Game.lives[name][1])%100
        y = (Game.lives[name][2])%100
        Game.Map[x][y] = [] 
        Game.lives.pop(name)
        
    def IA(name):
        class BackgroundTasks(threading.Thread):
            def run(self,*args,**kwargs):
                while True:
                    time.sleep(0.5)
                    if Fight.WhoIsInNineByNine(name) != []:
                        Fight.Attack(name)
                    
                    mobLife = Game.lives[name][0]
                    if mobLife <= 0:
                        mob.depop(name)
                        bonus.heart.pop(mob.spawn,Game.lives[Game.player][0]//2, Game.lives[Game.player][0]//5)
                        break
                    
                    xplayer = Game.lives[Game.player][1]
                    yplayer = Game.lives[Game.player][2]
                    xmob = Game.lives[name][1]
                    ymob = Game.lives[name][2]
                    
                    if xplayer == xmob and yplayer == ymob:
                        Fight.TakesDammage(name, 1)
                        Fight.TakesDammage(Game.player, 1)
                        mob.up(name)
                    coor =  deplacement.CoorSet
                    
                    coor = deplacement.goto(xmob, ymob, xplayer, yplayer)
                    mob.goto(coor[0], coor[1], name)
                    
        t = BackgroundTasks()
        t.start()
        
    def spawn(life = 5, dammage = 1):
        name = f"MOB"
        x = random.randint(0,9)
        y = random.randint(0,9)
        Game.lives[name]=(life, x, y, dammage)
        Game.Map[x][y] = '◌'
        mob.IA(name)