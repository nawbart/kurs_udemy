class book:
    title = ""                  #Tytuł
    number_of_pages = None      #ilosc stron
    author = ""                 #autor
    release_date = None         #data wydania
    owner = ""                  #wlasciciel

    # **** a to jest nasz konstruktor ****

    def __init__(self, p1, p2, p3):
        self.imie = p1
        self.wiek = p2
        self.plec = p3

    def przywitaj(self):
        print("Cześć. Mam na imię", self.imie)

    def ruszaj(self):
        if self.plec == "kobieta":
            print("Ruszyłam w drogę")
        else:
            print("Ryszyłem w drogę")

    def mysl(self):
        if self.wiek < 2:
            print("Dopiero się ucze")
        else:
            print("Nie ma problemu")