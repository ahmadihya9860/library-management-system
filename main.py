from book import Book
from member import Member
from library import Library



def main():
    # create library object
    library = Library("shool library")
    print(f"welcome to {library.name}")
    
    # create member objects
    member_1 = Member(name="ahmad")
    member_2 = Member(name="mohamad")
    member_3 = Member(name="alli")
    
    # create book objects
    book1 = Book("python","Guido van rossum")
    book2 = Book("C","Dennis Ritchie")
    book3 = Book("Rust","Graydon Hoare")
    
    # add the book to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # add the members to library 
    library.add_member(member_1)
    library.add_member(member_2)
    library.add_member(member_3)
    
    # priting the books available in the library
    library.show_books()
    
    # view users
    library.show_members()
    
    

main()