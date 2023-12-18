#Show user menu
#give user ability to input items into cart
#menu items with prices 
#ability to add/delete/view and quit 
#Show items in shopping cart
#reciept. total amount

def grocery_shopping():
    menu = {
                'chicken': 7.00,
                'steak': 8.00,
                'salmon': 11.00,
                'rice': 6.50,
                'beans': .99,
                'potato': 1.00,
                'spinach': 3.25,
                'marinade': 9.75,
                'broccoli': 2.50,
                'corn': .79,
    }

    total = 0
    shopping_cart = []

    print()
    print('===== MENU=====')

    for key, value in menu.items():
        print(f"{key}: {value}")
    
    # ask user how they would like to move forward
    while True:
        user_input = input('What would you like to do? Add/Remove/View Cart/Receipt/Quit ').lower()
        if user_input == 'quit':
            break   
        elif user_input == 'add':
    # ask user what they want to add to cart
            add_item = input('Enter menu items to add to cart: ')
    #check if the iem is in the menu
        if add_item in menu:
            shopping_cart.append(add_item)
            total += menu[add_item]
            print()
            print(f'\n{add_item} added to cart. Total: ${total:.2f}')
        else:
            print('Invalid item. Please choose from the menu')
        if user_input == 'remove':
    # ask user what item they want to remove
            remove_item = input('Enter menu item to remove from cart: ')
    #remove specified item from shopping_cart
        shopping_cart.remove(remove_item)
        total -= menu[remove_item]
        print()
        print(f'{remove_item} removed from cart. Total: ${total:.2f}')
        if user_input == 'view cart':
        #if shopping_cart:
            print('====SHOPPING CART====')
        for item in shopping_cart:
            print(f'{item}: ${menu[item]:.2f}')
            print(f'Total: {total:.2f}')
        else:
            print('The cart is empty')
        if user_input == 'receipt':
            if shopping_cart:
                print('======RECEIPT======')
                print(f'Total: {total:.2f}')
        else:
            print('The cart is empty. No receipt.')
    else:
        print('INVALID COMMAND. Please enter Add, Remove, or Quit.')
        
grocery_shopping()