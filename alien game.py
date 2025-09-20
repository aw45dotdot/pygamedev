import pgzrun,random
TITLE = "shoot the alien"
WIDTH = 700
HEIGHT = 700
msg = ' '
alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color=(253,157,159))
    alien.draw()                              #make alien visible
    screen.draw.text(msg,center=(330,20),fontsize=30,color="black")
    
    
    
def place_alien():
    alien.x = random.randint(50,700)
    alien.y = random.randint(50,700)
    
    
def on_mouse_down(pos):
        global msg
        if alien.collidepoint(pos):
            msg = "YOU CLICKED THE ALIEN"
            place_alien()
            
        else:
            msg = "YOU DIDN'T CLICK THE ALIEN TRY AGAIN"
            

place_alien()    




pgzrun.go()
