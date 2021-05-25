# imports random word for creating a new dictionary
from random_word import RandomWords
r = RandomWords()

#Create a string, a list, a dictionary
#1. Declare the data manually

my_string = 'This is mine!'
my_list = [1,2,3,4,5,6,7,8,9,10]
my_dictionary = {"name": "brandon", "occupation": "Awesome"}

#2. Use a loop to declare the data

for item in [my_string, my_list, my_dictionary] :
    print(item)

#Create a function that turns 3 strings into a list

def list_it (string1, string2, string3):
    return [string1, string2, string3]
#Create a dictionary from 2 lists
my_keys = my_dictionary.keys()
my_values = my_dictionary.values()

my_new_dictionary = dict(zip(my_keys, my_values))

print(my_new_dictionary, "my new dictionary")

#Create a dictionary using loops
ind = 0
random_dictionary = {}
while ind < 10 :
    random_dictionary[ind] = r.get_random_word()
    ind += 1

print(random_dictionary, "my random dictionary")
#Import a .txt file. Iteratate through the data, creating a list of all strings that start with "S". Print the list.
infile = open("BillOfRights.txt", "r") 
   
content = []

plist = infile.readline()
while plist:
    if(plist[0].lower() == 's'):
        content.append(plist)
    plist = infile.readline()

infile.close()
print(content)

#Use 3 inputs, send the strings to a function, have the function return a list of the inputs
string1 = input("gimmie string\n")
string2 = input("gimmie string again\n")
string3 = input("gimmie string AGAIN AGAIN\n")
def list_it(one, two, three):
    return [one, two, three]

three_string_list = list_it(string1, string2, string3)
print(three_string_list)
#Create a code that has 2 functions. Have one call the other as part of the code.
def get_numbers():
    str_num1 = input("Give me number now\n")
    str_num2 = input("GIMMIE ANOTHER\n")
    return [int(str_num1), int(str_num2)]

def add_dem():
    list_of_numbers = get_numbers()
    return list_of_numbers[0] + list_of_numbers[1]

added_value = add_dem()
print(added_value)

