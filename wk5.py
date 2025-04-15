
#Base class - has basic info about book
class Book:
    def __init__(self,tittle,author,genre):
        self.tittle = tittle
        self.author = author
        self.genre = genre

        # describes the book 

    def describe(self):  
        print(f"'{self.tittle}' is a {self.genre} book written by {self.author}")
    
    #generic read action
    def read(self):
        print(f"Reading'{self.tittle}'....")
       

# Subclass Ebook

class EBook(Book):
    def __init__(self, tittle, author, genre,file_size):
        super().__init__(tittle, author, genre)

        self.file_size = file_size 

    def read(self):
        print(f"Opening the eBook '{self.tittle}'(File size:{self.file_size}MB) on your device.")

# Subclass :AudioBook
class AudioBook(Book):
    def __init__(self, tittle, author, genre, length):
        super().__init__(tittle, author, genre)

        self.length = length 
    
    def read(self):
        print(f"Playing audiobook '{self.tittle}' ({self.length} minutes long.) ")


#book objects to be used for this program
my_book = Book("Digital Dawn","Ava Reed","Sci-Fi")
my_Ebook = EBook ("Digital Dawn","Ava Reed","Sci-Fi",5)
my_Audiobook = AudioBook("Voices of the past","Liam Stone", "Historical",120)


# usecase examples
my_book.describe()
my_book.read()

my_Ebook.describe()  
my_Ebook.read()


my_Audiobook.describe()  
my_Audiobook.read()