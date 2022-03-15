import ast 
import sys
#open text file in read mode
text_inventory = open("The inventory complete", "r")
 
#read whole file to a string
extract_inventory = str(text_inventory.read())

#close file
text_inventory.close()

# this is the inventory:
inventory_dict = ast.literal_eval(extract_inventory)

while True:
    user_input2 =input('remove, show, quit, or add item: ')

    if user_input2 == 'remove':
        print(' ')
        print ('--- the inventory ---')
        for key, value in inventory_dict.items():
         print(key, ' : ', value)
        print(' ')
        remove_what2 = input('what do you want to remove: ')
        if remove_what2 in inventory_dict:
            removed_item = inventory_dict.pop(remove_what2)
        else:
            print('that isnt in the inventory')

    elif user_input2 == 'quit':
        print('program has quit')
        print(' ')
        print('--- the inventory ---')
        for key, value in inventory_dict.items():
         print(key, ' : ', value)
        print(' ')
        print('The inventory will be printed into a .txt file.')
        reset_value = sys.stdout 

        with open('The inventory complete', 'w') as f:
            sys.stdout = f 
            print(inventory_dict)
            sys.stdout = reset_value 
        break

    elif user_input2 == 'show':
        print(' ')
        print('--- the inventory ---')
        for key, value in inventory_dict.items():
         print(key, ' : ', value)
        print(' ')

    else: 
        try:
            enter_price2 = int(input('Enter a price: '))
            inventory_dict[user_input2] = enter_price2
        except:
            print('only integers.')
