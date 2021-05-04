# def multiply_two_numbers(num1, num2) :
#     return num1 * num2

# print(multiply_two_numbers(3, 5))

def do_cube_things(num):
    accum = 0
    for ind in range(2) :
        if(ind == 0):
            accum += num * num
        else :
            accum = (accum * num)
    result = str(num) + ' cubed is ' + str(accum)
    return result

def cube_it():
    strNum = input('What number do you want cubed?')
    return do_cube_things(int(strNum))



print(cube_it())
