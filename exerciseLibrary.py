class LibraryBooks:
    def __init__(self):
        self.books = ["Book 1", "Book 2", "Book 3", "Book 4",]

    def displayBooks(self):
        print("The library have the following books\n")
        for book in self.books:
            print(book)

    def removeBook(self,requestBook):
        if requestBook in self.books:
            print("You have borrowed the following book: ", requestBook)
            self.books.remove(requestBook)




    def addBook(self,returnBook):
        self.books.append(returnBook)


class Customer:
    def requestBook(self):
        self.bookKey = input("Which book do you want to book out: ")
        return self.bookKey
    def returnBook(self):
        self.bookKey = input("What is the book's name you want to return: ")
        return self.bookKey


library = LibraryBooks()
customer = Customer()
choice = ""
while choice != 4:
    print("Please select a option", "\n"
            "1. Display Library Books", "\n"
            "2. Pick book you want", "\n"
            "3. Return an book", "\n"
            "4. Exit Program")
    choice = int(input("Please make a selection: "))
    if choice == 1:
        library.displayBooks()
    elif choice == 2:
        bookKey = customer.requestBook()
        library.removeBook(bookKey)
    elif choice == 3:
        bookKey = customer.returnBook()
        library.addBook(bookKey)
    elif choice != 4:
        break
    else:
        print("You havent made a choice")
