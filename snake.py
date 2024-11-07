"""
le snake - v0
on repeint l'écran à une période de 1 seconde
et on a du mal à sortir du programme
"""

# les imports standard en premier
from random import randint

import pygame as pg

# on initialise pygame et on crée une fenêtre de 400x300 pixels
pg.init()
screen = pg.display.set_mode((30*20, 30*20))

# on crée aussi un objet "horloge"
clock = pg.time.Clock()
snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]
FRUIT = (randint(0,30),randint(0,30))
direction = (1,0)
fruitcolor = (255,0,0)
# enfin on boucle à l'infini pour faire le rendu de chaque image
running = True
while running == True:
    # l'objet "clock" permet de limiter le nombre d'images par secondes
    # ici pour cette démo on demande 1 image par seconde
    clock.tick(3)
    if -1 in snake[0] :
            running = False
    elif 31 in snake[0] :
            running = False 
    # il faut traiter les événements a minima
    # pour que la fenêtre s'affiche
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP :
                direction = (0,-1)
            elif event.key == pg.K_DOWN :
                direction = (0,1)
            elif event.key == pg.K_LEFT :
                direction = (-1,0)
            elif event.key == pg.K_RIGHT :
                direction = (1,0)
            # si la touche est "Q" on veut quitter le programme
            elif event.key == pg.K_q:
                running = False
    if FRUIT == snake[-1] :
        snake.insert(0,FRUIT)
        FRUIT = (randint(0,30),randint(0,30))
    
     

   # les coordonnées de rectangle que l'on dessine
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    
    # appel à la méthode draw.rect()
    color = (255, 255, 255) # couleur blanche
    snakecolor = (0,255,0)
    screen.fill((0,0,0))
    for i in range(15) :
        for j in range(30) :
            if j%2 == 1 :
                x = 2*i*height # coordonnée x (colonnes) en pixels
                y = j*width # coordonnée y (lignes) en pixels
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect)
            else :
                x = 2*i*height + 20 # coordonnée x (colonnes) en pixels
                y = j*width # coordonnée y (lignes) en pixels
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect)

   

    
    snake.append(tuple(a + b for a, b in zip(snake[-1], direction))) # type: ignore
    snake.pop(0)
    for i in range(len(snake)) :
        pg.draw.rect(screen,snakecolor,pg.Rect(snake[i][0]*20,snake[i][1]*20,width,height))

    pg.draw.rect(screen,fruitcolor,pg.Rect(FRUIT[0]*20,FRUIT[1]*20,width,height))
    # enfin on met à jour la fenêtre avec tous les changements
    pg.display.update()