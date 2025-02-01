class book():
    def __init__(self):
        self.title=input("Enter the title:")
        self.author=input("Enter the author:")
        self.isbn=input("Enter the ISBN:")
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("ISBN:",self.isbn)
obj=book()
obj.display()