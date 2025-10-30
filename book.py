
class Book:
    book_id = 0
    def __init__(self,title,auther):
        Book.book_id +=1
        
        self.title = title
        self.auther = auther
        self.id = Book.book_id
        self.status = True
    
    def schow_info(self):
        # the method fro schow detils about book
        print(f"title {self.title}\nauther {self.auther}\nid {self.id}\nstatus {self.status}")
    
    
    def borrow(self):
        self.status = False
        
    
    def return_book(self):
        self.status = True
            

