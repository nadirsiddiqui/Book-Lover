import pandas as pd

class BookLover:
    
    def __init__(self, 
                 name, 
                 email, 
                 fav_genre, 
                 num_books = 0, 
                 book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def addbook(self, book_name, book_rating):
        if book_rating > 5 or book_rating < 0:
            return "Please enter a rating between 0 and 5"  
        elif isinstance(book_name, str) != True:
            return "Please enter a string for Book Name"
        elif book_name in set(self.book_list['book_name']):
            return "This book is already in your book list"
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
        
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books += 1
    
    def has_read(self, book_name):
        if book_name in set(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
             
