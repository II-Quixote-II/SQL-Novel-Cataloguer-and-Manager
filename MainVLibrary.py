# CLI Menu Plan

"""
1) Add a book
2) List all books
3) Search by title
4) Update read status
5) Update rating
6) Delete a book
7) Quit
""" 

------------------------------------------------------------------------------

import VirtualLibrary as library

def print_books(books) -> None:
    if not books:
        print("(no books found)")
        return
    for b in books:
      
# Adding after fix bugs
      
