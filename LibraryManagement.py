class Library:

    def __init__(self, list1):
        self.allbooks = list1
        self.availablebooks = list1[:]
        self.bookslent = {}

    def display_allbooks(self):
        for books in self.allbooks:
            print(books)

    def display_availablebooks(self):
        for books in self.availablebooks:
            print(books)

    def borrowbook(self, book_name, user_name):
        if book_name not in self.availablebooks:
            print("Enter the correct BookName!")
            return

        if book_name in self.availablebooks:
            self.bookslent.update({book_name: user_name})
            self.availablebooks.remove(book_name)
            print("You can take the book")
        else:
            print("Sorry!The book is already taken by " + self.bookslent.get(book_name))

    def returnbook(self, book_name):
        if book_name not in self.allbooks:
            print("Enter the correct BookName!")
            return

        if book_name in self.bookslent:
            user_name = self.bookslent.pop(book_name)
            self.availablebooks.append(book_name)
            print(f"Thank you for returning the book, {user_name}.")
        else:
            print("Book not found in the lent books list")


if __name__ == "__main__":
    list1 = ["The Lincoln Highway", "This Time Tomorrow", "Book Lovers", "The Judge's List", "A Monster Calls",
             "Skulduggery Pleasant", "Refugee Boy"]
    lib = Library(list1)
    while True:
        print("Welcome to Library. Enter an option")
        print("1. Display all books")
        print("2. Display available books")
        print("3. Borrow the book")
        print("4. Return the book")
        print("5. Quit")

        user_choice = int(input())
        if user_choice == 1:
            lib.display_allbooks()
        elif user_choice == 2:
            lib.display_availablebooks()
        elif user_choice == 3:
            user_name = input("Enter the UserName:")
            book_name = input("Enter the BookName:")
            lib.borrowbook(book_name, user_name)
        elif user_choice == 4:
            book_name = input("Enter the BookName:")
            lib.returnbook(book_name)
        elif user_choice == 5:
            break
        else:
            print("Enter a valid Choice:")
