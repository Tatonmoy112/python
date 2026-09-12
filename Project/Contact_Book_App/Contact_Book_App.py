contact={}

while True:
    choice=int(input("1.Add New Contact.\n"
                 "2.Search Contact.\n"
                 "3.Display Contact.\n"
                 "4.Edit Contact.\n"
                 "5.Delete Contact.\n"
                 "6.Exit.\n"
                 "Please enter number between 1-6: "))
    # print("--------------------------------")
    if choice==1:
        name=input("Enter your name: ")
        num=input("Enter your phone number: ")
        contact.update({name:num})
        print("New contact successfully insert Contact Book.")
        print("--------------------------------")
    if choice==2:
        name=input("Enter the name of perosn: ")
        print(f"Here is information:\nName: {name}\nNumber: {contact.get(name)}")
        print("--------------------------------")
    if choice==3:
        print(f"Here is all contact: {contact}")
        print("--------------------------------")
    if choice==4:
        i=input("Which contact you want to change? ")
        n=input("Enter new number: ")
        contact[i]=n
        print("New number successfully insert in Contact Book.")
        print("--------------------------------")
    if choice==5:
        i=input("Which contact you want to delete? ")
        del contact[i]
        print("Successfully delete from Contact Book.")
        print("--------------------------------")
    if choice==6:
        print("You quit from the contact.")
        print("--------------------------------")
        break