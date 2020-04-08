def setup ():
    size (400,600)
    point (50,50)
    line (100,100,50,50)
def draw ():
    print (height, width, mouseX, mouseY, mousePressed)
    line (height, width, mouseX, mouseY)
    rect (100, 100, 50, 50)
    if mousePressed:
        line (height/8,width/8,mouseX,mouseY)
    else:
        rect (mouseX,mouseY,height/8,width/8)
    

        
        
