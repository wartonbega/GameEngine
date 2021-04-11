#!/usr/bin/env python
    

def show(Map, playerLife, playerName, lives):
    print('\n---------------------------------\n')
    AllLives = list(lives.keys())
    for a in range(len(AllLives)):
        if AllLives[a] == playerName:
            AllLives.pop(a)
            break
    playerStat = lives[playerName]
    life=''
    
    print(f'\n {playerName} life : \n')
    for x in range(playerLife):
        life+='♥'
    print(life)
    
            
    for i in Map:
        for x in i:
            if x == []:
                print(' ', end=' ')
            else:
                print(x,end=' ')
        print()
    print(f'{playerStat}')
    
    


    
