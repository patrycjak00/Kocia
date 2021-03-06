# aby dobrzeoddać abstrakcję, trzeba przemyśleć wybór klas, aby dobrze obrazowały rzeczywisty model, a metody umieścić tak, aby odpowiedzialność poszczególnych podmiotów się zgadzała
import unittest

class Library(): # aplikacja zarzdza zasobami biblioteki, więc klasy to biblioteka i klient
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): # biblioteka umożliwia wypożyczenie z niej książki
        if requestedBook in self.availableBooks: # o ile taka istnieje i jest dostępna
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): # przejrzenie zasobu
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): # przeywrócenie książki do zasobu
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): # klient ma wiele cech, ale z perspektywy biblioteki interesuje nas tylko czy ma wypożyczoną książę i jeśli tak to jaką
    book = "" # ten typ biblioteki umożliwia wypożyczenie jedne książki jednej osobie
    haveBook = False
    def requestBook(self, book): # klient może zapytać o książę
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): # albo zwrócić jeśli posiada
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False

def setup():
    size(220,100)
    global library, Madzia
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
    library = Library(books) # bo biblioteka bez książek, to nie biblioteka
    Madzia = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): # poklikajcie kilkakrotnie w przyciski: wypożyczneie dwa razy tej samej książki, próba zwrócenia bez posiadania żadnej? Kto podejmuje działanie? 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc")) # cała interakcja między biblioteką a klientem łączy się dopiero tutaj, obiekty są oddzielne i każdy ma swoją odpowiedzialność: biblioteka za przechowywane książki, klient za wypożyczoną i to tej odpowiedzialności dotyczą metody, nie używają wzajemnie swoich pól, jest porządek
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            
                    
class TestClass(unittest.TestCase):
    
    def setUp(self): # to nie jest zbyt dobra praktyka, testy powinny  być od siebie niezależne, a więc obiekty tworzonebezpśrednio w testach
        self.Madzia = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        self.library = Library(books) # bo biblioteka bez książek, to nie biblioteka
        
        
    def test_lendBook(self):
        # testujemy czy książka została wypożyczona poprawnie
        self.library.lendBook(self.Madzia.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], self.library.availableBooks)   
         
        # testujemy teraz czy książka została przypisana do obiektu Customer
        self.assertEqual(self.Madzia.book, "Harry Potter")
        self.assertTrue(self.Madzia.haveBook)
        
    def test_addBook(self):
        # testujemy czy poprawnie można dodać książkę do biblioteki
        self.library.addBook("Pan Tadeusz")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Pan Tadeusz"], self.library.availableBooks)
        
    def test_returnBook(self):
        # test dotyczący zwrotu książki do biblioteki
        self.Madzia.haveBook=True
        self.Madzia.book = "Wiedzmin"
        self.library.addBook(self.Madzia.returnBook())
        
        self.assertFalse(self.Madzia.haveBook)
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "Wiedzmin"], self.library.availableBooks)
        
if __name__ == '__main__': # brakowało tego do uruchomienia
    unittest.main()
    
#generalnie testy dobre :)
# 1,75pkt +
