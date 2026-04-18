from .book import Book

class Library(Book):
    def __init__(self,book_serial_number,title,author):
        super().__init__(title,author)
        self.book_serial_number = book_serial_number
    
    def show_information_library(self):
        print('The print is from library:',self.book_serial_number,' title ',self.title)
        
obj1= Library('101','physics','jeorge')
obj1.show_information_library()

            
            

        


