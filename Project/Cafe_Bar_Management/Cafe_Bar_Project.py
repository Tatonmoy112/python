class Menus:
    def __init__(self):
        self.menu={
            "Pizza": 500,
            "Burger": 280,
            "Salad": 200,
            "Coffe": 220,
            "Sub": 240
        }
class Order(Menus):
    def __init__(self):
        super().__init__()
        self.order_num = 0
        self.order_list = []
        self.order_bill = 0

    def take_order(self):
        while True:
            if self.order_num == 0:
                self.order_num+=1
                print("Welcome to our Cafe Bar.")
                self.display_menu()
                item=self.order_items()
                quantity=self.quantity_items()
                self.confirm_order(item,quantity)
                print(f"Order of {quantity} : {item.capitalize()} has been added.")
                print("----------")
            else:
                extra=input("Do you want to order anything else? (Yes/No) ")
                if extra.capitalize()=='Yes' or extra.capitalize()=='Y':
                    item=self.order_items()
                    quantity=self.quantity_items()
                    self.confirm_order(item,quantity)
                    print(f"Order of {quantity} : {item.capitalize()} has been added.")
                    print("----------")
                    
                elif extra.capitalize()=='No' or extra.capitalize()=='N':
                    self.total_bill()
                    break
                elif extra.capitalize() not in ('Yes','No','Y','N'):
                    print("Invalid input. Please answer Yes or No.")


    def display_menu(self):
        for item, price in self.menu.items():
            print(f"{item} : {price}")

    def order_items(self):
        while True:
            item=input("Enter the item you want to order: ").capitalize()
            if item in self.menu:
                return item
            else:
                print("Invalid item. Please choose from the menu.")

    def quantity_items(self):
        while True:
            try:
                quantity=int(input("Quantity: "))
                if quantity>0:
                    return quantity
                else:
                    print("Invalid quantity. Please enter positive number.")
            except:
                print("Invalid input. Please enter a valid number.")

    def confirm_order(self,item,quantity):
        self.order_list.append((item,quantity))
        self.order_bill += self.menu[item]*quantity
    
    def total_bill(self):
        print("----------\nYour bill details:")
        for item , quantity in self.order_list:
            print(f"{quantity} x {item} : {self.menu[item] * quantity}")
        print(f"Total bill: {self.order_bill}")
        print("----------")


order1=Order()
order1.take_order()











# menu = {
#     "Pizza": 500,
#     "Burger": 280,
#     "Salad": 200,
#     "Coffe": 220,
#     "Sub": 240
# }
# order_num = 0
# order = False
# order_bill=0
# while not order:
#     if order_num == 0:
#         order_num+=1
#         ipt=input("Welcome to our Cafe Bar. Here's the menu:\n"
#         "Pizza: 500\n"
#         "Burger: 280\n"
#         "Salad: 200\n"
#         "Coffe: 220\n"
#         "Sub: 240\n"
#         "Enter your first item you want to order: ")
#         quantity=int(input("Quantity:"))
#         order_bill=order_bill + (menu.get(ipt.capitalize()) * quantity)
#         print(f"Order of {ipt.capitalize()} has been added.")
#         print("----------")
#     if order_num > 0:
#         extra=input("Do you want to order anythinh else? ")
#         if extra=='Yes' or extra=='yes' or extra=='Y' or extra=='y':
#             ipt2=input("Enter item for order: ")
#             quantity=int(input("Quantity:"))
#             order_bill=order_bill + (menu.get(ipt2.capitalize()) * quantity)
#             print(f"Your order of {ipt2.capitalize()} has been added.")
#             print("----------")
#         else:
#             print("----------------------------------\n"
#                   f"The Total price to pay is {order_bill}\n"
#                   "Thank you for your order.\n"
#                   "----------------------------------")
#             order=True