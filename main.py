from src.models.book import Book
from src.models.dvd import DVD
from src.user.user import User
from src.services.library import Library 

# Create library
library = Library()

# Create items
book1 = Book("Python Basics", 1, "John Smith", 300)
dvd1 = DVD("Inception", 2, 120, "Sci-Fi")

library.add_item(book1)
library.add_item(dvd1)
print()

# Create user
user = User("Erik")
# Borrow items
user.borrow_item(book1)

print()

# Show borrowed items

user.list_borrowed_items()
print()

# return items
user.return_item(book1)

print()

# show library_items
library.display_all_items()

print(library)
            
           
