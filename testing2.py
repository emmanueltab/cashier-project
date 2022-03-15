the_inventory = {'hh' : 99}

# prints stuff into txt file
import sys

print('The inventory will be printed into a .txtt file.')

reset_value = sys.stdout # Save a reference to the original standard output

with open('The inventory complete', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(the_inventory)
    sys.stdout = reset_value # Reset the standard output to its original value

# converts string to dictonary 

import json

str = '{"Name": "Millie", "Age": 18, "City": "Atlanata"}'

print('The JSON String is', str)

convertedDict = json.loads(str)

print("After conversion: ", convertedDict)
print(type(convertedDict))

# extracts data from txt file
a_file = open("fdr_inaugural_address.txt")
file_contents = a_file.read()

print(file_contents)