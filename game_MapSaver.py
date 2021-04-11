#!/usr/bin/env python
import ast
def save(classe):
    file = open('GameSave.ge','w')
    file.write('lives\n'+str(classe.lives)+ '\n_\n'+ 'maxMap\n'+str(classe.maxMap)+ '\n_\n'+ 'player\n'+str(classe.player)+'\n_\n'+ 'allSkin\n'+ str(classe.allSkin)+ '\n_\n'+'playerSkin\n'+ str(classe.playerSkin)+ '\n_\n'+'playerPointing\n'+ str(classe.playerPointing)+ '\n_\n'+'obstacles\n'+ str(classe.obstacles) +'\n_\n'+ 'water\n'+ str(classe.water)+ '\n_\n'+'structure\n'+ str(classe.structures)+'\n_\n'+'Map\n'+ str(classe.Map))
    file.close()

class ToReturn:
    lives = ''
    maxMap = ''
    player = ''
    allSkin = ''
    playerSkin = ''
    playerPointing = ''
    obstacles = ''
    water = ''
    structures = ''
    Map = ''

def reuse():
    file = open('GameSave.ge','r')
    content = file.read()
    file.close()
#    res = ast.literal_eval(content)
    Var = content.split('\n_\n')
    for i in Var:
        ToSplit = i.split('\n')
        if ToSplit[0] == 'lives':
            ToReturn.lives = ast.literal_eval(ToSplit[1])
        elif ToSplit[0] == 'maxMap':
            ToReturn.maxMap = int(ToSplit[1])
        elif ToSplit[0] == 'player':
            ToReturn.player = ToSplit[1]
        elif ToSplit[0] == 'allSkin':
            ToReturn.allSkin = ast.literal_eval(ToSplit[1])
        elif ToSplit[0] == 'playerSkin':
            ToReturn.playerPointing = ToSplit[1]
        elif ToSplit[0] == 'playerPointing':
            ToReturn.playerPointing = ToSplit[1]
        elif ToSplit[0] == 'obstacles':
            ToReturn.obstacles = ast.literal_eval(ToSplit[1])
        elif ToSplit[0] == 'water':
            ToReturn.water = ast.literal_eval(ToSplit[1])
        elif ToSplit[0] == 'structure':
            ToReturn.structures = ast.literal_eval(ToSplit[1])
        elif ToSplit[0] == 'Map':
            ToReturn.Map = ast.literal_eval(ToSplit[1])
    return ToReturn