class Book:
    def __init__(self, title:str, auther:str, pages:str):
        self.title = title
        self.auther = auther
        self.pages = pages

    def read_pages(self,num_pages:int):
        self.pages -=num_pages
        if self.pages <= 0:
            print('You have finished reading the book!')
        else:
            print(f"You have {self.pages} pages left.")


        
my_book = Book("1984", "George Orwell", 100)
my_book.read_pages(30)
my_book.read_pages(70)
my_book.read_pages(10)