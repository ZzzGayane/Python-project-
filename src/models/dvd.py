from src.models.library_item import LibraryItem

class DVD(LibraryItem):
  def __init__(self, title, item_id, duration, genre):
    super().__init__(title, item_id)
    self.duration = duration
    self.genre = genre
  def display_info(self):
    super().display_info()
    print("Duration:", self.duration)
    print("Genre:", self.genre)
  def borrow(self):
    if self.available:
      self.available = False
      print(f"{self.title} has been borrowed")
    else:
      print(f"{self.title} is already borrowed")
  def return_item(self):
    self.available = True
    print(f"{self.title} has been returned")
    
  
