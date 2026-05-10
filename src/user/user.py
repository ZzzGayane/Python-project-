class User:
  def __init__(self, name):
    self.name = name
    self.borrowed_items = []
  def borrow_item(self, item):
    if item.available:
      item.borrow()
      self.borrowed_items.append(item)
      print(f"User {self.name} borrowed: {item.title}")
    else:
      print(f"{item.title} is not available")
  def return_item(self, item):
    if item in self.borrowed_items:
      item.return_item()
      self.borrowed_items.remove(item)
      print(f"User {self.name} returned: {item.title}")
    else:
      print(f"{self.name} did not borrow this item")

  def list_borrowed_items(self):
    print(f"{self.name}'s borrowed items:")
    for item in self.borrowed_items:
      print("-", item.title)
    
