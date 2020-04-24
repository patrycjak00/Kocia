add_library('pdf') 
def setup():
    #size(600, 800, PDF, "outZad.pdf")
    size(500, 500) 
    global tlo
    global i1
    global i2
    tlo = loadImage("tlo.jpg")
    i1 = loadImage("wasy.png")
    i2 = loadImage("oksy.png")
    
    beginRecord(PDF, "outZad.pdf")
    
def draw():
    global tlo
    global i1
    global i2
    image(tlo, 0,0, 500, 500) 
    image(i1,480,600, 100, 100)
    image(i2,480,600, 100, 100)

    endRecord() 

    if keyPressed:
        if key == "z":

             image(i1, 110,320, 300, 100)    
        if key == "x":
             image(i2, 60,180, 400, 200)
      
