import pgzrun
import random

WIDTH = 1080
HEIGHT = 720

def draw():
    r=255
    g=0
    b=random.randint(0,255)

    w = WIDTH - 200
    h = HEIGHT - 200
    
    for i in range(20):
          rect = Rect((0,0),(w,h))
          rect.center = 1080,720
          screen.draw.rect(rect,(r,g,b))
          
          r -= 10
          g += 10
          w -= 10
          h -= 10




pgzrun.go()
