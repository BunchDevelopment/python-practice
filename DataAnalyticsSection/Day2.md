Night 2
***Indexing and Slicing:***
Which integer does indexing begin with?
0

Given the following array:
 flowers = np.array([[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]])
 How do we access number 55 (with indices)?
flowers[2][2]
How do we access the entire first row?
flowers[0]?

Bonus:
 How do we access the entire first row as a 2D array?
 <!-- ! -->

How do we return the entire first row with slicing?
flowers[:]

Does indexing/slicing return a view or a copy?
copy

Use slicing to select the first two rows. flowers[:2]
Use slicing to select the last two rows. flowers[-2:]
Use slicing to select the last columns of the last two rows. flowers[-2:][-1]
Copying Arrays:
When would you use views?
when you want a shallow copy

When would you use copies?
when you want a deep copy

***Boolean Indexing:***
Given the following array:
 flowers = np.array([[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]])
 Identify all flowers divisible by 5. flowers[flowers % 5 == 0]
 Identify all even flowers.flowers[flowers % 2 == 0]
 Identify all flowers less than 42. flowers[flowers < 42]
 Use ~ to identify flowers greater than 42. flowers[~flowers < 42]
 Use a condition to identify flowers divisible by 5. flowers[flowers % 5 == 0]
 Replace all flowers divisible by 3 with 0’s. flowers[(flowers % 3 == 0) = 0]
 You’re in a PE class, and you can satisfy your class requirement with the following options, but you’re very picky about your physical activity. 
 Let’s query our arrays to find something you’d like to do for class. 
 Given the following arrays:
exercises = np.array([“running”, “gymnastics”, “basketball”, “weights”,“hiking”])
locations = np.array([“outside”, “inside”, “inside”, “inside”, “outside”])
minutes = np.array([30, 45, 45, 30, 60])
Find all outside activities. 
exercises[locations == "outside"]

Find all outside activities less than 30 minutes because it’s hot out there.It’s a rainy day and you want to play inside in the gym. What is the duration of a basketball game?
exercises[(locations == "outside") & (minutes < 30)]

Which activities can you do inside for 45 minutes?
gymnastics, basketball

You have extra energy to burn (lucky you). Which activity has the longest duration requirement?
hiking

You have to leave school early today. Which activity can you do in under 30 minutes?
none

Where, any, all...Given the following array:
rents = np.array([1250, 800, 750, 775, 1100, 1150, 1250, 750])
Determine where the cheap rents (less than $1000) are located in the array.
Are there any rents that cost $1250?
1,2,3,7

Are all rents greater than $1000?
0, 4,5,6

Are all rents greater than $500?
yes

***Fancy Indexing***
Given the following array: 
x = np.array([9, 0, 95, 84, 65, 52, 44, 73, 6, 20])
Pass an array of indices to find the values at 7, 5, 8, and 1.
x[7,5,8,1]
Pass a 2d nparray to find the values at 7, 5, 8, and 1 and describe its shape.
ind2 = np.array([7,5,8,1])
x[ind2]