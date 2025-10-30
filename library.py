from member import Member
from book import Book

class Library:
    def __init__(self,name):
        self.name = name
        self.members = []
        self.books = []
    
    
    
    def add_book(self,book):
        self.books.append(book)
        
        
    def add_member(self,member):
        self.members.append(member)
    
    def search_book(self,title):
        for book in self.books:
            if book.title == title:
                print(f"title {book.title}\nauther {book.auther}\nid {book.id}")
            
            else:
                print("not found")
    
    def show_books(self):
        for book in self.books:
            print("---------")
            print(f"{book.title} => auther -> {book.auther} => id {book.id}")
            
    def show_members(self):
        for member in self.members:
            print(f"{member.name} => id {member.id}")
            
