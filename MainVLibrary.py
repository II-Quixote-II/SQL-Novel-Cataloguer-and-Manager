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
        rating = b["Rating"] if b["Rating"] is not None else "-"
        genre = b["Genre"] if b["Genre"] else "-"
        print(f'  [{b["id"]}] {b["Title"]} by {b["Author"]}  '
              f'({b["Read_status"]}, genre: {genre}, rating: {rating})')


def main() -> None:
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            read_status = input("Read_Status (optional): ").strip() or None
            rating = input("Rating (optional): ").strip() or None
            genre = input("Genre (optional): ").strip() or None
            date_started = input("Date_Started (optional): ").strip() or None
            date_finished = input("Date_Finished (optional): ").strip() or None
            
            book_id = library.add_book(title, author, read_status, rating, genre, date_started, date_finished)
            print(f"Added '{title}' with id {book_id}")
            

      
