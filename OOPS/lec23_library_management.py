class Library:
    def __init__(self):
        self.noBooks=0
        self.books= []
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def getbook(self):
        book=input("enter the book you want: ")
        if book in self.books:
            print("yes you can take")
            self.books.remove(book)
            self.noBooks-=1
        else:
            print("The book is not available")
    def showinfo(self):
        print(f"The library has {self.noBooks} books and have ")
        for book in self.books:
            print(book)       

l1=Library()
l1.addBook("Harry Porter")
l1.addBook("Life")
l1.addBook("Beauty and beast")
l1.getbook()
l1.addBook("The wings of fire")
l1.showinfo()



