import random
import pgzrun #import modules

WIDTH = 600  #screen settings
HEIGHT = 500

Bumbleebee = Actor("bee")  #variable assigned to picture
Flower = Actor("flower")

score = 0

Bumbleebee.pos = 100,100
Flower.pos = 200,300   #characrter positoning on screen

def draw():
    screen.blit("bg",(0,0))     #show screen bg from file
    Flower.draw()               #show flower and bumblebee
    Bumbleebee.draw()
    screen.draw.text("score = "+str(score),center=(330,20),fontsize=30,color="black")

def update(): 
    global score
    if keyboard.left:
        Bumbleebee.x = Bumbleebee.x -2      #keyboard key assiging
    if keyboard.right:
        Bumbleebee.x = Bumbleebee.x +2
    if keyboard.up:
        Bumbleebee.y = Bumbleebee.y -2
    if keyboard.down:
        Bumbleebee.y = Bumbleebee.y +2
    flowercollect = Bumbleebee.colliderect(Flower)
    if flowercollect:
        Flower.x = random.randint(50,550)
        Flower.y = random.randint(50,450)
        score +=1
    

pgzrun.go()             #run program
