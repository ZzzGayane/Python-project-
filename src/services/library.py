class Library:

  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)
    print(f"{item.title} added to library")

  def remove_item(self, item):
    if item in self.items:
      self.items.remove(item)
      print(f"{item.title} removed from library")

  def search_item(self, title):
    for item in self.items:
      if item.title == title:
        return item
    return None

  def display_all_items(self):
    print("Library items:")
    for item in self.items:
      item.display_info()
      print("-----")

  def __len__(self):
    return len(self.items)
  def __str__(self):
    return f"Library contains {len(self.items)} items"
