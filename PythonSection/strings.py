import random
#Here we create a string, assigning it to a variable
astr = "Hello my name is Brandon."

#Printing the string
print(astr)

#Let's try looping through the string, printing each element. What happens?
for x in range(len(astr)):
    print(astr[x])

#Let's create a substring and see if it is "in" the longer string
bstr = "Thomas"
if bstr in astr:
    print("That is a substring.")
if bstr not in astr:
    print("That is not a substring.")

#Let's create a substring and see if it is "in" the longer string
cstr = "bra"
if cstr in astr.lower():
    print("That is a substring.")
if cstr not in astr:
    print("That is not a substring.")

#Let's demonstrate slicing a string:
dstr = astr[3:10]
print(dstr)

estr = astr[:4]
print(estr)

fstr = astr[5:]
print(fstr)

#CODE CHALLENGE#

#Can you do this: Crate a program, with a function. The function will test if one string is a subset of another.

def check_is_digit(input_str):
    if input_str.strip().isdigit():
        return True

    else:
        return False


def slice_it_up(string_to_slice, slice_start, slice_end):
    test_start = check_is_digit(slice_start)
    test_end = check_is_digit(slice_end)

    if test_end and test_start:
        start = int(slice_start)
        end = int(slice_end)
        print("The slice of the string is: ", string_to_slice[start: end])

    else :
        print('for wanting a hint, you didnt give me a good number... *insert eye roll emoji*')

def is_subset(str1, str2):
    if str1 is '':
        print('Missing required params')

    elif str1.lower() in str2.lower():
        print('Ey, thats in the string! You get a smiley face :)')

    else:
        print("awe...that isn't in the string. You're a failure. Take this sad face :(")
        user_want_hint = input('Do you want a hint?\n')

        if user_want_hint.lower() in 'yes':
            start = input('Where do you want me to start to slice?\n')
            end = input('Where do you want me to end it?\n')
            slice_it_up(str2, start, end)

first_string = input('What string do you think is in my hidden string?\n')
my_string = 'May the 4th be with you my dude.'

is_subset(first_string, my_string)

#It will return true or false.
#In the main body ask for input.
#Use the input to test the input string against the one you chose.
#Have the program print whether it is a substring or not.

my_random_number = random.randint(1, 100)
first_guess = input('Welcome!\n Try and guess my number! \nWhat is your first guess?\n')
#! LETS GOOOOOOO FIRST RECURSIVE FUNCTION IN PYTHON MY DUDE
def check_number():
    if check_is_digit(first_guess):
        parsed_first = int(first_guess)
        if parsed_first == my_random_number :
            print('Omg you actually guessed it first try!')
        else:
            guess = input('try again:')
            if check_is_digit(guess):
                guess = int(guess)
                if guess == my_random_number:
                    print('there you go!')
                else: 
                    if guess < my_random_number:
                        print('higher!')
                    elif guess > my_random_number:
                        print('lower!')
                    check_number()
            else:
                print('that isnt a number...')
    else:
        print('that isnt a number...')
check_number()
