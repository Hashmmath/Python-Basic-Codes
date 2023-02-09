shopping_cart = []

def display_menu():
    print("1. Bananas - $0.49")
    print("2. Apples - $0.99")
    print("3. Oranges - $0.59")
    print("4. Grapes - $1.99")
    print("5. Mangoes - $1.49")
    print("6. Pineapple - $2.99")
    print("7. Peaches - $1.99")
    print("8. Plums - $1.49")
    print("9. Pears - $0.99")
    print("10. Kiwis - $0.79")
    print("11. View Cart")
    print("12. Checkout")

def add_to_cart(item_number):
    if item_number == 1:
        shopping_cart.append(("Bananas", 0.49))
    elif item_number == 2:
        shopping_cart.append(("Apples", 0.99))
    elif item_number == 3:
        shopping_cart.append(("Oranges", 0.59))
    elif item_number == 4:
        shopping_cart.append(("Grapes", 1.99))
    elif item_number == 5:
        shopping_cart.append(("Mangoes", 1.49))
    elif item_number == 6:
        shopping_cart.append(("Pineapple", 2.99))
    elif item_number == 7:
        shopping_cart.append(("Peaches", 1.99))
    elif item_number == 8:
        shopping_cart.append(("Plums", 1.49))
    elif item_number == 9:
        shopping_cart.append(("Pears", 0.99))
    elif item_number == 10:
        shopping_cart.append(("Kiwis", 0.79))

def view_cart():
    print("Your Shopping Cart:")
    for item in shopping_cart:
        print(item[0] + " - $" + str(item[1]))

def checkout():
    total = 0
    for item in shopping_cart:
        total += item[1]
    print("Total: $" + str(total))

while True:
    display_menu()
    choice = int(input("Enter your choice (1-12): "))
    if choice == 11:
        view_cart()
    elif choice == 12:
        checkout()
        break
    else:
        add_to_cart(choice)

'''This code defines a shopping_cart list that will store the 
items the user adds to their cart. The display_menu function 
displays the list of items and their prices. The add_to_cart 
function adds the selected item to the shopping cart. The 
view_cart function displays the contents of the shopping cart, 
and the checkout function calculates and displays the total 
price of the items in the cart. The code runs in a while loop 
that continues until the user chooses to checkout (choice 12).'''