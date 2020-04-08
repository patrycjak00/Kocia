def setup():
    global x, y # nie mamy pewności, że będąc po za funkcą setup inicjalizacja tych zmiennych wykoan się na początku programu. Przy przepełnieniu pamięci, mogłoby to być później, a wtedy użycie ich w ciele funkcji draw dałoby błąd.
    x= 200
    y=400
    size(400,400)
    stroke(255,0,0)
    strokeWeight(3)
    frameRate(30)

def draw():
    global slownik
    slownik={"czerwony":(225,0,0), "niebieski":(0,0,225), "zielony":(0,225,0)}
   
    stroke(*slownik["zielony"])
    global lista
    lista=[]
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    fill(*lista[y%len(lista)])
    global x
    global y
    rect(x,y,30,30)
    x += 1
    y += 1
    if x > width/2: # teraz lepiej widać, że chodzi o połowę szerokości, i w razie zmiany jej wielkości wciąż bęzie działać
        y += -2
    if y < height/2:
        x += -2
    rect(x,y,8,8)
    print(y, x)
    
def mousePressed():
    exit()
    
# 2pkt
