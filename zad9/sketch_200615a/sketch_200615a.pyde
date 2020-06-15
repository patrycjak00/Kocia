def setup():
    
    size(1200, 1600)
    
    
    
def draw():
    global img
    img = loadImage("image.jpg")
    
    image(img, 50,100, 500,500)
    
    try:
        f= open("image.jpg")
        if f.name == "image.jpg":
            raise Exception 
            
except FileNotFoundError as e:
    print(e)
except Exception as e: 
    print ("Bład! zla_nazwa")
    print rect(50,100,500,500)
    fill (255,0,0,90)
    
    else:
        print rect(50,100,500,500)
        fill (0,0,255,0)
        stroke(0,0,255)
    finally:
        print("zakonczono")
