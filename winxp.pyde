def setup():
    dead = False
    size(640, 480)
    background(0xff, 0xff, 0xff)
    img = loadImage("desktop.jpg")
    image(img, 0, 0)
            
def draw():
    global dead
    if not dead:
        fill(0xff,0xff,0xff)
        rect(mouseX, mouseY, 50, 40)
        fill(0xee, 0xee, 0xee)
        rect(mouseX, mouseY, 50, 10)
        textSize(10)
        fill(0,0,0)
        text("-[]x", mouseX+33, mouseY+10)
    if mousePressed:
        dead = True
        background(0,0,0xff)
        textSize(24)
        fill(0xff,0xff,0xff)
        text(";(\nYour PC is dead\n* press any key to crash again", 20, 40, 500, 500) 
        
dead = False
frame = 0
