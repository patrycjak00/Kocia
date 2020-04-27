def setup():
    size(500, 500)
    textSize(200) 
def draw():
    clear()

    s = createShape()
    s.beginShape()
    s.fill(38,88,51,200) 
    s.stroke(33,32,1,255)
    s.vertex(100, 320) 
    s.vertex(420,320) 
    s.vertex(270,350) 
    s.endShape(CLOSE)
    shape(s, 0, 0)  
    if keyPressed: # te miały zmieniać zaznaczenie z jednej litery na drugą, a działa też gdy nic nie jest zaznaczone
        if keyCode == LEFT:
            fill(100, 20, 22, 500)
            text("P", width/2-100, height/2+50)
        if keyCode == RIGHT:
            fill(100, 20, 22, 500)
            text("K", width/2, height/2+50)        
    if mousePressed : # miało być na najechanie myszą i sama litera imienia
        fill(100, 20, 22, 150)
        text("P", width/2-100, height/2+50)
        text("K", width/2, height/2+50)
    if keyPressed:
        key == "k"
        if key == "k":
            fill(13, 100, 100, 1000)
            text("K", width/2, height/2+50)                            
    e = createShape()
    e.beginShape()
    e.fill(38,88,51,200) 
    e.stroke(33,32,1,255)
    e.vertex(100, 120) 
    e.vertex(420,120) 
    e.vertex(270,90) 
    e.endShape(CLOSE)
    shape(e, 0, 0)
     
# 1,25p    
