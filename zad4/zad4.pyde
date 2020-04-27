add_library('pdf') 
def setup():
    #size(600, 800, PDF, "outZad.pdf")
    size(400, 500) # prawdziwa proporcja zdjęcia dokumentowego
    global tlo, i1, i2 # można jednolinijkowo
    tlo = loadImage("tlo.jpg")
    i1 = loadImage("wasy.png")
    i2 = loadImage("oksy.png")
    
    beginRecord(PDF, "outZad.pdf")
    
def draw():
    global tlo, i1, i2
    image(tlo, 0,0, tlo.width, tlo.height) # obraz o wielkosci oryginalnego

    if keyPressed: # wartoby wypisać użytkownikowi jakie ma opcje w programie
        if key == "z":
            image(i1, 110,320, 300, 100) 
        if key == "x":
            image(i2, 60,180, 400, 200)
        endRecord()  # teraz pdf się zapisze dopiero po dorysowaniu grafiki, nie przed 

# 1p
