global szerokosc
global wysokosc
szerokosc = 600
wysokosc = 600
class Pkt(object): # zwyczajowo nazwy klas z dużej litery; w pythonie 2 było wymagane podanie object w nawiasie przy definicji klasy; coono oznacza będzie w kolejnym temacie
    ##STRZALKI##
    left = 0 # dzięki temu, że robimy z nich atrybuty klasy, są wspólne dla wszystkich obiektów
    right= 0
    down = 0
    up = 0
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed= 11
        self.h = 40
        self.w = 40
    def show(self):
        fill(170,100,100)
        rect(self.x,self.y,self.w,self.h)
    def update(self, speed):
        self.speed = speed
        self.x = self.x + (Pkt.right - Pkt.left)*self.speed
        self.y = self.y + (Pkt.down - Pkt.up)*self.speed
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
    global a, b
    a = Pkt()
    b = Pkt() # miały być dwa obiekty, a to uwidacznia często błędy
    
def draw():
    background(100)
    a.show()
    a.update(5)
    b.show()
    b.update(10)
    
def keyPressed():
    if keyCode == UP:
        Pkt.up=1
    if keyCode == DOWN:
        Pkt.down=1
    if keyCode == LEFT:
        Pkt.left=1
    if keyCode == RIGHT:
        Pkt.right=1
        
def keyReleased():
    if keyCode == UP:
        Pkt.up=0
    if keyCode == DOWN:
        Pkt.down=0
    if keyCode == LEFT:
        Pkt.left=0
    if keyCode == RIGHT:
        Pkt.right=0
        
# 1,5pkt
