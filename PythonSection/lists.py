#Here I set up lists. They can contain many different types of data.
alst = [1, "2", "Three", 3.34]
blst = ["Seven", 2, 77.3]

#Here I print the lists.
print(len(alst))
print(len(blst))

#Here I loop or iterate through the lists and print each element of them.
for elem in alst:
    print(elem)

for elem2 in blst:
    print(elem2)

#Here I create a new list add add to it by looping through the first 2 lists
newlst = []

for elem in alst:
    newlst.append(elem)
for elem2 in blst:
    newlst.append(elem2)

print(newlst)

#Here I show how to index a list:

print(alst[1])

print(blst[1])


##CODE CHALLENGE: CREATE THREE LISTS. CREATE A FOURTH LIST WITH NO ELEMENTS. USING LOOPS, ADD THE ELEMENTS OF ALL THREE LISTS TO THE FOURTH LIST. PUSH THIS TO YOUR REPO.

list1 = [1,2,3,4,5,6,7]
list2 = ['one', 'two', 'three']
list3 = ["hey", "what", "is", "good", "my", "dude"]
def test ():
    return True

def test2 ():
    return False

list4 = [test(), test2()]
print(list4)

combo_list = []

for item in list1:
    combo_list.append(item)
for item in list2: 
    combo_list.append(item)
for item in list3: 
    combo_list.append(item)
print(combo_list)