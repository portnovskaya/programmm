import random
napis = ['SAMBUKA', 'LEMON', 'SOL']
def draw (): 
    if mousePressed:
        print(random.choice(napis))
    else:
        print('You have to press')
