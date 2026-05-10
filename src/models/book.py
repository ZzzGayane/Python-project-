from src.models.library_item import LibraryItem

class Book(LibraryItem):
  def __init__(self, title, item_id, author, pages):
    super().__init__(title, item_id)
    self.author = author
    self.pages = pages
  def display_info(self):
    super().display_info()
    print("Author:", self.author)
    print("Pages:", self.pages)

  def borrow(self):
    if self.available:
      self.available = False
      print(f"{self.title} has been borrowed")
    else:
      print(f"{self.title} is already borrowed")
  
  def return_item(self):
    self.available = True
    print(f"{self.title} has been returned")
