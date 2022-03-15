# this adds stuff to a dictonary:

scones = {
	"Fruit": 22,
	"Plain": 14,
	"Cinnamon": 4,
	"Cheese": 21
}

scones["Cherry"] = 10

print(scones)
print(' ')



# this prints dictonaries clealy:

student_score = {   'Ritika': 5,
                    'Sam': 7, 
                    'John': 10, 
                    'Aadi': 8}

for key, value in student_score.items():
    print(key, ' : ', value)
print(' ')

# used to remove things from a dictionary:

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
print ("The dictionary before performing remove is : " + str(test_dict))
removed_value = test_dict.pop('Mani')
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))
print ('\r')
removed_value = test_dict.pop('Manjeet', 'No Key found')
print ("The dictionary after remove is : " + str(test_dict))
print ("The removed key's value is : " + str(removed_value))


# used to prevent users from inputing a number:
a = 0
while a != 2:
	user_input = input('enter something: ')
	a = 1 + a
	try:
		int(user_input) 
	except:
		pass
	else:
		print('that cannot be a number.')
			

# prevents the user from inputing an non integer:
inventory = {'hhh' : 444}
enter_price = 99
try:
 enter_price = int(input('Enter a price: '))
 inventory[user_input] = enter_price
except:
	print('only integers.')

			
        

	
			
    
		


