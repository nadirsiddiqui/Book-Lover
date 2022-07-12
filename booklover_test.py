import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        lover1.addbook('Invisible Cities', 5)
        actual =  'Invisible Cities' in set(lover1.book_list.book_name)
        expected = True
        self.assertEqual(actual, expected)
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        lover1.addbook('Invisible Cities', 5)        
        lover1.addbook('Invisible Cities', 5)
        
        x = lover1.book_list.book_name.value_counts() > 1
        actual = True in x.values
        expected = False
        self.assertEqual(actual, expected)
        

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        lover1.addbook('Invisible Cities', 5)  
        actual = lover1.has_read('Invisible Cities')
        
        expected = True
        self.assertEqual(actual, expected)
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        
        testValue = lover1.has_read('Invisible Cities')
        message = 'Test Value is not False'
        self.assertFalse(testValue, message)
        
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        lover1.addbook('Invisible Cities', 5) 
        lover1.addbook('Percy Jackson', 4)
        lover1.addbook('Harry Potter', 4)
        
        expected = 3
        actual = lover1.num_books_read()
        self.assertEqual(actual, expected)
        
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        lover1 = BookLover('Nadir', 'nhs2bc@virginia.edu', 'fantasy')
        lover1.addbook('Invisible Cities', 5) 
        lover1.addbook('Percy Jackson', 4)
        lover1.addbook('Freakonomics', 3)
        
        actual = False in (lover1.fav_books().book_rating.values > 3)
        expected = False
        self.assertEqual(actual, expected)
        
            
if __name__ == '__main__':
    
    unittest.main(verbosity=3)