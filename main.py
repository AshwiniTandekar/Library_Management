class Library():
    def __init__(self,list_of_book,library_name):
        self.list_of_book=list_of_book
        self.library_name=library_name
        self.lend={}
    def display_book(self):
        """Displaying the library's books"""
        print("This Books Are Available:")
        for index,books in enumerate(self.list_of_book):
            print(f"{index} : {books}")
    def lend_book(self,person,book):
        """Function for Receiving books"""
        if book in self.list_of_book or person not in self.list_of_book:
            if book not in self.lend.keys():
                self.lend.update({book:person})
                print("The Book Is Listed By Your Name")
            else:
                print(f"Sorry, This Book {book} is not in {self.library_name}\nIt Has Given To {self.lend[lending_book_name]}")
        else:
            print("Invalid Input\nPlease Check The Display Block")
    def add_book(self,donate_book_name):
        """You Have Donate book in library"""
        self.list_of_book.append(donate_book_name)
        print("You Donate Successfully\n Thanks For Donating")
    def return_book(self,book_name):
        """Function For returning book"""
        if book_name in self.lend.keys():
            self.lend.pop(book_name)
            print(f"The {book_name} Book Has Been Returned Successfully!\nThank You for being responsible!")
        else:
            print("This Book is Already Returned or Perhaps You Entered wrong input \n")
if __name__ == '__main__':
    obj=Library(["Felling Is The Secret", "Believe In Yourself", "Learning How To Fly", "Wings Of Fire"],"Ashwini Library")
    print(f"Welcome To The {obj.library_name}")
    print("You Choose The Right Place ")
    print("Choose Option:")
    while True:
        print("---Press 1 Display Books ")
        print("---Press 2 Lend Book ")
        print("---Press 3 Add Book")
        print("---Press 4 Return Book")
        user = int(input("Enter Your Choice :"))
        if user==1:
            obj.display_book()
        elif user==2:
            lending_book_name = input("Which Book Do You Want To Lend :").capitalize()
            lending_person_name = input("Enter Your Name :").capitalize()
            obj.lend_book(lending_person_name,lending_book_name)
        elif user==3:
            d_input= input("Enter Book Name That You Want To Donate: ").capitalize()
            obj.add_book(d_input)
        elif user==4:
            r_input= input("Enter Book Name You Want To Return:").capitalize()
            obj.return_book(r_input)
        else:
            print("Invalid Input!")
        a=input("Press q to quit and any key for continue:\n")
        if a=="q":
            exit()
        else:
            continue

