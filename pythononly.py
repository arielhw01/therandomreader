import random
import json
from prettytable import PrettyTable
from termcolor import colored

# JSON Functions to Load and Save Books
def load_books_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file is not found
    
def save_books_json(file_path, books):
    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)


# File path for storing book data
file_path = '/Users/arielwong/code/cip_project/books.json'

# Load existing books or an empty list if file does not exist
books = load_books_json(file_path)

def prettytable(input):
    table = PrettyTable()
    table.title = 'Books'
    keys = input[0].keys()
    
    table.field_names = keys
    
    for row in input:
        values = row.values()
        table.add_row(values)

    print(table)

prettytable(books)    
    

def main_menu():
    while True:
        print(colored('\nWelcome to your TBR assistant!\n', 'blue', attrs=['bold']))

        menu_table = PrettyTable()
        menu_table.title = 'Menu'
        menu_table.header = False
        menu_table.add_row(['1', 'TBR Pile'])
        menu_table.add_row(['2', 'Add Book'])
        menu_table.add_row(['3', 'Update Book Progress'])
        menu_table.add_row(['4', 'TBR Progress'])
        menu_table.add_row(['5', 'Choose Your Next Read'])
        menu_table.add_row(['6', 'Quit'])

        print(menu_table)
        choice = input('\nEnter your choice (1-6): ')
        
        if choice == '1':
            show_tbr_pile()
            return_to_menu()
            break
        elif choice == '2':
            add_book()
            break
        elif choice == '3':
            update_book()
            return_to_menu()
            break
        elif choice == '4':
            show_tbr_progress()
            break
        elif choice == '5':
            next_read()
            break
        elif choice == '6':
            print('\nExiting...Happy reading!\n')
            break
        else:
            print('Invalid choice, please enter a number between 1 and 6.')

def show_tbr_pile():
    print('\nYour TBR Pile:')
    display_books_table(books)

def display_books_table(book_list):
    if not book_list:
        print('No books to display.')
        return

    table = PrettyTable()
    table.title = 'Books'
    keys = book_list[0].keys()
    
    table.field_names = keys
    
    for row in book_list:
        values = row.values()
        table.add_row(values)

    print(table)


def add_book():
    # check if tbr is at the limit
    books_tbr = len([book for book in books if not ['completed']])
    if len([book for book in books if not book['completed']]) >= 50:
        print("\nYou have reached the 50-book limit! Consider finishing or removing some books first.")
        return

    title = input("\nEnter the book title: ")
    genre = input("Enter the book genre: ")
    new_id = max(book['id'] for book in books) + 1 if books else 1
    books.append({"id": new_id, "title": title, "genre": genre, "completed": False, "skipped": False})
    print(f"\nBook '{title}' added to your TBR list!")
    save_books_json(file_path, books)  # Save after adding a book

    return_to_menu()


def return_to_menu():
    return_to_menu = input('\nPress enter to return to the main menu.')
    if return_to_menu == '':
        main_menu()

def update_book():
    print("\nWhich book would you like to update?")
    display_books_table(books)

    try:
        book_id = int(input("Enter the Book ID to mark as completed or skip: "))
        for book in books:
            if book['id'] == book_id:
                action = input("Enter 'c' to mark as completed or 's' to skip: ").lower()
                if action == 'c':
                    book['completed'] = True
                    print(f"Book '{book['title']}' marked as completed.")
                elif action == 's':
                    book['skipped'] = True
                    print(f"Book '{book['title']}' marked as skipped.")
                break
        else:
            print("No book found with that ID.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    save_books_json(file_path, books)

# choose my next read
def next_read():
    books_in_tbr = [book for book in books if not book['completed']]
    if not books_in_tbr:
        print("\nThere are no books in the list! Add books to get started.")
        return
    user_next_read = random.choice(books_in_tbr)
    print(f"\nNext Read: {user_next_read['title']}\n")

    return_to_menu()


# progress (%) tbr completed
def show_tbr_progress():
    completed_books = len([book for book in books if book['completed']])
    total = len(books)
    percent_completed = (completed_books / total) * 100 if total > 0 else 0
    print(f"\nTBR Completion: {percent_completed:.0f}% ({completed_books}/{total} books)") 

    return_to_menu()

# skips
def skip():
    pass

# gpt for short descriptions
# def gpt_description(title):
    # description = call_gpt(title)
    # print(f"Description of '{title}': {description}")

# show book list

def main():
    main_menu()

if __name__ == '__main__':
    main()
