def setup():
    size(1200, 1600)
    noFill()
def draw():
    global img
    img = loadImage("image.jpg")
    try:
        image(img, 50,100, 500,500)
    except: 
        print ("Bład! zla_nazwa")
        print 
        stroke (255,0,0,90)
    else:
        stroke(0,0,255)
    finally:
        rect(50,100,500,500)
        print("zakonczono")
        
#1pkt
