def setup ():
    size (400,600)
    point (50,50)
    line (100,100,50,50)
    rect (100, 100, 50, 50) # tu nie ma zmiennych, więc rónie dobrze można narysować raz na wstępie, zamiast co klatkę
def draw ():
    print (height, width, mouseX, mouseY, mousePressed)
    line (height, width, mouseX, mouseY)
    if mousePressed:
        line (height/8,width/8,mouseX,mouseY)
    else:
        rect (mouseX,mouseY,height/8,width/8)
# 2 pkt
    

        
        
