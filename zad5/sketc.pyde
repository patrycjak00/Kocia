global szerokosc
global wysokosc
szerokosc = 600
wysokosc = 600
class pkt(object):
    ##STRZALKI##
    def __init__(self):
        self.x = 10
        self.y = 10
        self.up = 0
        self.left = 0
        self.right= 0
        self.down = 0
        self.speed= 11
        self.h = 40
        self.w = 40
    def show(self):
        fill(170,100,100)
        rect(self.x,self.y,self.w,self.h)
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed
        self.y = self.y + (self.down - self.up)*self.speed
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= (szerokosc - self.w)):
            self.x = (szerokosc - self.w)
        if not (self.y >= 0):
            self.y = 0
        if not (self.y <= (wysokosc - self.h)):
            self.y = (wysokosc - self.h)


def setup():
    size(szerokosc,wysokosc)
    global a
    a = pkt()
    
def draw():
    background(100)
    a.show()
    a.update()
    
def keyPressed():
    if keyCode == UP:
        a.up=1
    if keyCode == DOWN:
        a.down=1
    if keyCode == LEFT:
        a.left=1
    if keyCode == RIGHT:
        a.right=1
        
def keyReleased():
    if keyCode == UP:
        a.up=0
    if keyCode == DOWN:
        a.down=0
    if keyCode == LEFT:
        a.left=0
    if keyCode == RIGHT:
        a.right=0
