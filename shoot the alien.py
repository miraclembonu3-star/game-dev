import pgzrun
import random

WIDTH = 600
HEIGHT = 500

alien = Actor("alien")
alien.pos = 300,300
score = 0


def draw():
    screen.fill("violet")
    screen.draw.text("SHOOT THE ALIEN",(250,70),color="blue")
    alien.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.x = random.randint(50,550)
        alien.y = random.randint(50,450)


def update():
    pass

pgzrun.go()