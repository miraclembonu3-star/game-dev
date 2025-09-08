import pgzrun
import random

HEIGHT = 300
WIDTH  = 300


def draw():
    screen.fill("black")
    w = WIDTH
    h = HEIGHT - 200    
    for i in range(15):
        r = 255
        g = 0
        b = random.randint(120,255)
        rect = Rect((0,0),(w,h))
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))
        w=w-10
        h=h+10
        r=r-10
        g=g+10
        b=b-10
        
    



pgzrun.go()