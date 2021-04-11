#!/usr/bin/env python
import random

class geometry:
    def Square(size, x, y, door = True):
        structure = []
        for i in range(size):
            structure.append((x+i,y))
            structure.append((x, y+i))
            structure.append((x+i, y+size-1))
            structure.append((x+size-1, y+i))
        if door:
            structure.remove(random.choice(structure[4:-4]))
            
        return (structure, (x-1, y-1), (x+size+1, y+size+1))
        
class structure:
        
    def Mansion(max, map):
        x = random.randint(10, max-10)
        y = random.randint(10, max-10)
        mansion = [(x,y), (x+1,y), (x+2,y), (x+3,y), (x+4,y), (x+5,y), (x+6,y), 
                   (x,y+1), (x+6,y+1), 
                   (x,y+2), (x+6,y+2), 
                   (x,y+3), (x+1,y+3), (x+2,y+3), (x+4,y+3), (x+5,y+3), (x+6,y+3)]
        return (mansion, (x-1, y-2), (x+7, y+4))
    def Castle(max, map):
        x = random.randint(10, max-10)
        y = random.randint(10, max-10)
        castle = [(x,y+5), (x,y+6), (x,y+7), (x,y+8), (x,y+9), (x,y+10), (x,y+11), (x,y+12), (x,y+13), (x,y+14), (x,y+15), (x,y+16),
                  (x+1,y), (x+1,y+1), (x+1,y+2), (x+1,y+3), (x+1,y+4), (x+1,y+5), (x+1,y+16),
                  (x+2,y), (x+2,y+5), (x+2,y+16),
                  (x+3,y), (x+3,y+16), (x+3,y+17), (x+3,y+18), (x+3,y+19),
                  (x+4,y), (x+4,y+5), (x+4,y+19),
                  (x+5,y), (x+5,y+5), (x+5,y+16), (x+5,y+19),
                  (x+6,y), (x+6,y+1), (x+6,y+2), (x+6,y+3), (x+6,y+4), (x+6,y+5), (x+6,y+16), (x+6,y+17), (x+6,y+18), (x+6,y+19),
                  (x+7,y+5), (x+7,y+16), 
                  (x+8,y+5), (x+8,y+6), (x+8,y+7), (x+8,y+8), (x+8,y+9), (x+8,y+10), (x+8,y+12), (x+8,y+13), (x+8,y+14), (x+8,y+15), (x+8,y+16),
                  (x+9,y+10), (x+9,y+12)]
        return (castle, (x-1, y-2), (x+9, y+19))
