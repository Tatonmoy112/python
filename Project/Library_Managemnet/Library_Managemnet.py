class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    
    def add_book(self,b):
        self.books.append(b)
        self.no_of_books=len(self.books)
    def check(self):
        if(len(self.books)==self.no_of_books):
            print("It's all ok.")
        else:
            print("I think there is some problem in your program.")
    def show(self):
        print(f"Total num of books {self.no_of_books} and The books are:")
        for book in self.books:
            print(book)


A1=Library()
A1.add_book("The ghost1")
A1.add_book("The ghost2")
A1.add_book("The ghost3")
A1.add_book("The ghost4")
A1.add_book("The ghost5")

A1.check()
A1.show()


# class Library:
#     no_of_books=0
#     books=[]
#     def __init__(self,b):
#         Library.no_of_books+=1
#         self.books.append(f"{Library.no_of_books}.{b}")
#     def check():
#         if(len(Library.books)==Library.no_of_books):
#             print("It's all ok.")
#         else:
#             print("I think there is some problem in your program.")
#     def show():
#         for i in Library.books:
#             print(i)


# Library1=Library("A")
# Library2=Library("B")
# Library3=Library("C")
# Library4=Library("D")
# Library5=Library("E")

# print(f"Total num of books:{Library.no_of_books}")
# print(Library.books)
# Library.show()