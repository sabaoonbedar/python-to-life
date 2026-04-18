class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrow = False

        
        
    def show_info(self):
        if self.is_borrow:
            print("the book is borrowed by someone")
        else:
            print("the book is available")
            print(f"Author: {self.author}")
            print(f"Title: {self.title}")
            

book1 = Book("the python life","sabaoon")
book2 = Book("the lady dada","Amjad")

book1.show_info()
book2.show_info()
        
        

        
                
