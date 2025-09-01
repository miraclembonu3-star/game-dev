import pgzrun

WIDTH=300
HEIGHT=300

def draw():
    screen.fill("white")
    screen.draw.circle((150,150),50,color="red")
    screen.draw.filled_circle((150,250),50,color="red")
    screen.draw.line((120,150),(50,50),"black")
    screen.draw.text("This is my first time doing this with visual studio",(250,300),color="black")



pgzrun.go()
