class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.author + " and " + other.author)

    def display(self):
        return self.title + " by " + self.author


book1 = Book("kruthik", "kruthikreddy")
book2 = Book("sri", "sri")

series = book1 + book2
print(series.display())