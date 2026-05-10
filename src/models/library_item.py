from abc import ABC, abstractmethod

class LibraryItem(ABC):
  def __init__(self, title, item_id):
    self.title = title
    self.item_id = item_id
    self.available = True
  def display_info(self):
    print("Title", self.title)
    print("Item_ID", self.item_id)
    print("Available", self.available)
    
  @abstractmethod
  def borrow(self):
    pass

  @abstractmethod
  def return_item(self):
    pass
