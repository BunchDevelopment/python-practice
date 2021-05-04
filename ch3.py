# Please debug these sections of code, until they work properly
# Section One
ans1 = input("Please enter one number: ")
ans2 = input("Please enter a second number: ")
an1 = int(ans1)
an2 = int(ans2)
sum1 = an1 + an2

print(sum1)

#Section Two
a = 3
b = 4.5

print(float(a) + b)

# Section Three
c = 0
v = 3.2
if c == 0 or v == 0:
    print('c or v is 0 which you cant divide by')
else: 
    print(v/c)

odd = 31
even = 5
for num in range(even):
    if num % 2 == 0:
        print(num, 'is and even number')
    else: 
        print(num, 'is and odd number')

l1 = ["5", "2", "3", "3.4", "apple", "CAR"]

if "1" in l1:
    print("Yes.")

if "1" not in l1:
    print("No.")

st1 = "mothersday"

if "day" in st1:
    print("Yes.")

if "day" not in st1:
    print("No.")

print(len(l1))

if len(l1) > 4:
    print("That list is long.")
if len(l1) < 5:
    print("The list is short.")