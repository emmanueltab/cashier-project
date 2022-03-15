inventory = {'cat' : 10, 'dog' : 20}
add_what = input('what do u want to buy: ')
total_cost = []

for key in inventory:
    if key in inventory:
        