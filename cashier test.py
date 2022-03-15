import ast
import sys

# this opens the inventory:

#open text file in read mode
text_inventory = open("The inventory complete", "r")
#read whole file to a string
extract_inventory = str(text_inventory.read())
#close file
text_inventory.close()
# this is the inventory:
inventory_dict = ast.literal_eval(extract_inventory)



# the shopping cart:
shopping_cart = []

# the total price variable:
total_price = []
print('Welcome to the shop, here are our options:', "\n")
        
print('--- the inventory ---')
for key, value in inventory_dict.items():
    print(f'{key}  :  {value}')
print(' ')

while True:
    user_input = input("what would you like to do? (do 'help' for commands): ")
    print(' ')
    if user_input == 'help':
        print('done - prints shopping cart onto .txt file and give reciept')
        print('inventory - shows the inventory')
        print('cart - shows the shopping cart')
        print('buy - adds item from inventory to shopping cart')
        print('total - shows the total price')
        print(' ')
        

    elif user_input == 'inventory':
        print('--- the inventory ---')  
        for key, value in inventory_dict.items():
            print(f'{key}  :  {value}')
        print(' ')

    elif user_input == 'buy':
        add_what = input('what would you like to buy: ')
        for value in inventory_dict:
            if value == add_what:
                shopping_cart.append(add_what)
                total_price.append(inventory_dict[value])
            else:
                print('that isnt available.')
                

    elif user_input == 'cart':
        print(f'your current shopping cart: {shopping_cart}')
        print(' ')

    elif user_input == 'total':
        total_cost = sum(total_price)
        print(f'your current total is {total_cost}')
        print(' ')

    elif user_input == 'done':
        break
            

            
            
        




        
        



        

