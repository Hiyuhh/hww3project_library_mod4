from cli import CLI
from classes import Book, User, Author

def library():
    books = [Book("The Great Gatsby", "F. Scott Fitzgerald","9781640322790", "Fiction", "1925", "Available"), Book("Love Her Wild", "Atticus", "9781501171239", "Poetry", "2017", "Available")]
    users = [User("Haya M.", "001"), User("Jakey L.", "002")]
    authors = [Author("F. Scott Fitzgerald", "Francis Scott Key Fitzgerald was an American novelist, essayist, screenwriter, and short-story writer."), Author("Atticus", "Atticus is a Canadian poet, writer, and Instagram personality.")]

    
    while True:
        try:
            CLI().display_menu() # Display the main menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Book Operations
                book_op(books, users)
            elif user_input == "2": # User Operations
                user_op(users) 
            elif user_input == "3": # Author Operations
                author_op(authors)
            elif user_input == "4": # Quit
                print("\nThank you for using the Library Management System! Goodbye! 👋\n")
                break 
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue


def book_op(books, users): # Method to handle book operations
    while True: 
        try:
            CLI().display_books() # Display the book operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new book
                add_book(books)
            elif user_input == "2": # Borrow a book
                borrow_book(books, users)
            elif user_input == "3": # Return a book
                return_book(books, users)
            elif user_input == "4": # Search for a book
                search_book(books, users)
            elif user_input == "5": # Display all books
                all_books(books)
            elif user_input == "6": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue

def user_op(users): # Method to handle user operations
    while True:
        try:
            CLI().display_users() # Display the user operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new user
                add_user(users)
            elif user_input == "2": # View user details
                user_details(users)
            elif user_input == "3": # Display all users
                all_users(users)
            elif user_input == "4": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue

def author_op(authors): # Method to handle author operations
    while True:
        try:
            CLI().display_authors() # Display the author operations menu
            user_input = input("\nWhat would you like to do?\n")
            if user_input == "1": # Add a new author
                add_author(authors)
            elif user_input == "2": # View author details
                author_details(authors)
            elif user_input == "3": # Display all authors
                all_authors(authors)
            elif user_input == "4": # Back to main menu
                break
            else: # Invalid input
                print("\n\n\nInvalid input.. Try again! ༼ つ ◕_◕ ༽つ")
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        
#----------------------------------------------------Methods for display_books----------------------------------------------------#
def  add_book(books): # Method to add a new book
    while True:
        try:
            title = input("\nWhat is the name of the book you would like to add? (Back)\n")
            if title.lower() == "back": # If user wants to go back to the main menu
                return 
            author = input("\nWho is the author of the book? ")
            ISBN = input("\nWhat is the ISBN of the book? ")
            genre = input("\nWhat is the genre of the book? ")
            publication_date = input("\nWhat is the publication date of the book? ")
            availability = True # Default availability of the book
            new_book = Book(title, author, ISBN, genre, publication_date, availability) # Create a new book object
            books.append(new_book)
            print(f"\nYou have successfully added '{title}' to the library! 📖\n")
            break # Back to main menu
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def borrow_book(books, users): # Method to borrow a book
    while True:
        try:
            title = input("\nWhat is the name of the book you would like to borrow? (Back)\n")
            if title.lower() == "back": # If user wants to go back to the main menu
                return
            unique_id = input("\nWhat is your Library ID: ")

            book_found = None # Initialize book_found to None
            for book in books: # Loop through the books
                if book.titles.lower() == title.lower(): # If the book is found
                    book_found = f"{book.titles} by {book.authors}" # Set book_found to the book by title and author
                    break
            if book_found:
                user_found = None # Initialize user_found to None
                for user in users: # Loop through the users
                    if user.get_library_id() == unique_id: # If the user is found
                        user_found = user # Set user_found to the user
                        break
                if user_found:
                        user_found.borrowed_books.append(book_found) # Add the book to the user's borrowed books list by title and author via book_found
                        book.availability = False # Set the book's availability to False
                        print(f"\n{user_found.get_name()}, you have successfully borrowed '{book_found}' from the library! 📖\n")                    
                        return                    
                else: # If the user is not found
                    print(f"\nSorry, you are not a registered user in the library.\n")
                    return
            else: # If the book is not found
                    print(f"\nSorry, '{title}' not found in the library or is unavailable.\n")
                    continue
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def return_book(books, users): # Method to return a book
    while True:
        try:
            title = input("\nWhat is the name of the book you would like to return? (Back)\n")
            if title.lower() == "back": # If user wants to go back to the main menu
                return
            unique_id = input("\nWhat is your Library ID: ")

            book_found = None # Initialize book_found to None
            for book in books: # Loop through the books
                if book.titles.lower() == title.lower(): # If the book is found
                    book_found = f"{book.titles} by {book.authors}" # Set book_found to the book by title and author
                    break
            if book_found: 
                user_found = None # Initialize user_found to None
                for user in users: # Loop through the users
                    if user.get_library_id() == unique_id: # If the user is found
                        user_found = user # Set user_found to the user
                        break
                if user_found:
                        user_found.borrowed_books.remove(book_found) # Remove the book from the user's borrowed books list by title and author via book_found
                        book.availability = True # Set the book's availability to True
                        print(f"\n{user_found.get_name()}, you have successfully returned '{book_found}' to the library! 📖\n")                    
                        return                    
                else: # If the user is not found
                    print(f"\nSorry, you are not a registered user in the library.\n")
                    return
            else: # If the book is not found
                    print(f"\nSorry, '{title}' is not in our library database. would you like to add the book? (Yes/No).\n")
                    user_input = input() # Ask the user if they would like to add the book
                    if user_input.lower() == "yes": # If the user wants to add the book
                        add_book(books) # Directs the user to the add_book method
                        return # Return to the main menu after adding the book
                    elif user_input.lower() == "no": # If the user does not want to add the book
                        continue # Continues to the beginning of the loop
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue 
        

def search_book(books, users): # Method to search for a book
    while True:
        try:
            search_input = input("\nWhat is the name of the book you would like to search for? (Back)\n")
            if search_input.lower() == "back": # If user wants to go back to the main menu
                return
            book_found = None # Initialize book_found to None
            for book in books: # Loop through the books
                if book.titles.lower() == search_input.lower(): # If the book is found
                    book_found = book # Set book_found to the book
                    break
            if book_found is not None: # If the book is found
                if book_found.availability: # If the book is available
                    print(f"\n📖 '{book_found}' is available in the library! Would you like to borrow it? (Yes/No)\n")
                    user_input = input() # Ask the user if they would like to borrow the book
                    if user_input.lower() == "yes": # If the user wants to borrow the book
                        borrow_book(books, users) # Directs the user to the borrow_book method
                        return # Return to the main menu after borrowing the book
                    elif user_input.lower() == "no": # If the user does not want to borrow the book
                        return # Return to the main menu
                else: # If the book is not available
                    print(f"\n📖 '{book_found}' is in our library database, but is currently being borrowed.\n")
            else: # If the book is not found
                print(f"\nSorry, '{search_input}' is not available in the library database.\n")
                continue
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def all_books(books): # Method to display all books
    while True:
        try:
            print("\nAll Books in the Library: 📚")
            if not books: # If there are no books in the library
                print("\n~There are no books in the library yet~")
            else: # If there are books in the library
                for book in books: # Loop through the books
                    availability = "Available" if book.availability else "Unavailable" # Set the availability of the book
                    print(f"📖 {book}, {book.genres}, {book.publication_dates}, {availability}")
            input("\nPress enter to go back  ") # Ask the user to press enter to go back to the main menu
            return # Return to the main menu
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        
# #-----------------------------------------------------------------------------------------------------------------------------------#

# #----------------------------------------------------Methods for display_users----------------------------------------------------#
def add_user(users): # Method to add a new user
    while True:
        try:
            name = input("\nWhat is your full name? (Back)\n")
            if name.lower() == "back": # If user wants to go back to the main menu
                return 
            unique_id = input("\nCreate a 3-4 digit Library ID # : ") 
            if len(unique_id) < 3 or len(unique_id) > 4: # If the length of the Library ID is less than 3 or greater than 4
                print("\nPlease enter a 3-4 digit Library ID #.\n")   
                continue # Redirect the user to the beginning of the loop to try again
            if any(user.get_library_id() == unique_id for user in users): # If the Library ID is already taken
                print("\nSorry, this Library ID is already taken. Please try again.\n")
                continue # Redirect the user to the beginning of the loop to try again
            new_user = User(name, unique_id) # Create a new user object
            users.append(new_user) # Add the new user to the users list
            print(f"\nYou have successfully added '{name}' to the library! 👥\n")
            return # Return to the main menu
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def user_details(users): # Method to view user details
    while True:
        try:
            search_input = input("\nWhat is the name of the user you would like to search for? (Back)\n")
            if search_input.lower() == "back": # If user wants to go back to the main menu
                return
            user_found = None # Initialize user_found to track if the user is found
            for user in users: # Loop through the users
                if user.get_name().lower() == search_input.lower(): # If the user is found 
                    user_found = user # Set user_found to the user to be searched for in the users list
                    break # Break the loop if the user is found
            if user_found is not None: # If the user is found 
                print(f"\n👥 {user_found.get_name()} has borrowed the following books:{user_found.borrowed_books}\n") 
                input("\nPress enter to go back  ") 
                return
            else: # If the user is not found
                print(f"\nSorry, '{search_input}' is not a registered user in the library.\n")
                continue 
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def all_users(users): # Method to display all users
    while True:
        try:
                print("\nAll Users in the Library: 👥")
                if not users: # If there are no users in the library
                    print("\n~There are no users in the library yet~")
                else: # If there are users in the library
                    for user in users: # Loop through the users
                        print(f"👥 {user.get_name()}, {user.get_library_id()}") # Using getter methods to get the privte attributes of user's name and Library ID
                input("\nPress enter to go back  ")
                return
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        
# #--------------------------------------------------------------------------------------------------------------------------------------#

# #----------------------------------------------------Methods for display_authors----------------------------------------------------#
def add_author(authors): # Method to add a new author
    while True:
        try:
            name = input("\nWhat is the name of the author you would like to add? (Back)\n")
            if name.lower() == "back": # If user wants to go back to the main menu
                return
            bio = input("\nWhat is the biography of the author? ")
            new_author = Author(name, bio) # Create a new author object
            authors.append(new_author) # Add the new author to the authors list
            print(f"\nYou have successfully added '{name}' to the library! 📚\n")
            return
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def author_details(authors): # Method to view author details
    while True:
        try:
            search_input = input("\nWhat is the name of the author you would like to search for? (Back)\n")
            if search_input.lower() == "back": # If user wants to go back to the main menu
                return
            author_found = None # Initialize author_found to track if the author is found
            for author in authors: # Loop through the authors
                if author.name.lower() == search_input.lower(): # If the author is found
                    author_found = author # Set author_found to the author to be searched for in the authors list
                    break
            if author_found is not None: # If the author is found
                print(f"\n📚 '{author_found.name}' Biography: {author_found.biography}\n")
                input("\nPress enter to go back  ")
                return
            else: # If the author is not found
                print(f"\nSorry, '{search_input}' is not an author in the library.\n")
                continue
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        

def all_authors(authors): # Method to display all authors
    while True:
        try:
            print("\nAll Authors in the Library: 📚")
            if not authors: # If there are no authors in the library
                print("\n~There are no authors in the library yet~")
            else: # If there are authors in the library
                for author in authors: # Loop through the authors
                    print(f"📚 {author.name}")
            input("\nPress enter to go back  ")
            return
        except Exception as e: # Error handling
            print(f"\n\n\n༼ つ ◕_◕ ༽つError: {e} ..Try again! ")
            continue
        
# #---------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__": # Run the library function
    library() 