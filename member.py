from book import Book


class Member:
    id = 0
    def __init__(self,name):
        Member.id +=1 
        self.name = name
        self.id = Member.id
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.status == True:
            book.borrow()
            print("you are borrow the book")
            self.borrowed_books.append(book)
        
        else:
            print("the book is not found")
    
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            
            
        else:
            print("you dont have the book in your borrowed list")

    def show_borrowed_books(self):
        print("_____________________________")
        for book in self.borrowed_books:
            print("---------")
            print(book.title)








