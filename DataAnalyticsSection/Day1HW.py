# Data Analysis Workflow: Summarize, in your own words, our 4-step process of data analysis. 
# - The 4 step process is gathering data, then getting that data into a uniform format, and as clean as possible, determining if you need more data to gather a conclusion, then getting a conclusion to gather a result. 

# What are some examples of roadblocks you might encounter? 
# - you might have issues finding data, data that is extremely dirty, issues finding patterns or missing key data

# How do you determine when you are finished analyzing the data?
# - did you gather a solid result from the data you interpreted? 

# What does “iterative” mean and how might it apply to your analysis process?
#  - its a flow that repeats until a condition is met. So you start from the beginning, and move step by step until you are satisified with the results

# Quantitative vs. Qualitative: Give 5 examples of quantitative qualities of trees, and 5 examples of qualitative qualities of trees. 
# - Quantitative: Number of trees, height of trees, average number of rings for trees, what time of the year each trees leaves start to turn yellow, time of year when trees start to bloom
# - Qualitative: the trees leaves are green, the trunk is brown, this tree came from spain, idk. 

# Which is better for data analysis? - Quantitative

# Name 3 studies on trees that could be possible. 
# - What trees bloom the earliest, trees average height based on type of tree, types of trees that turn yellow and when and possibly where.

# Which data is considered relevant? Which data is considered irrelevant? (Note: It definitely depends on the study you choose!)
# - Usually Quantitative data will be relevent. 

# Statistics and Analytics: There are several categories of statistics and analytics. Which type will we be using in this class? 
# -Descriptive Statistics ? 

# Name and describe 3 statistics calculations you are familiar with (If you do not know any, feel free to Google! We will cover them all in class.). 
# - the easy ones. Mean, median and Mode 

# Numpy:Import Numpy.Use your cli to get the version of Numpy you are using. 
# - 1.20.3

# Change each of these lists to npArrays. 
# How many dimensions do the following ndarrays have? 
# - 1,2,3,2
# Shape? 
# - (9,)
# - (3, 3)
# - (3, 2, 2)
# - (3, 2)
# Size? 
# - 9, 9, 12, 6
# Dtype?
# - int64, int64, int64, object
import numpy as np

things = [3, 4, 6, 4, 7, 1, 5, 7, 1]
stuff = [[3, 4, 6], [4, 7, 1], [5, 7, 1]]
ingredients = [[[3, 0], [4, 6]], [[4, 1], [7, 1]], [[5, 2], [ 7, 1]]]
elements = [[3, [4, 6]], [4, [7, 1]], [5, [ 7, 1]]]
npThings = np.array(things)
npStuff = np.array(stuff)
npIngredients = np.array(ingredients)
npElements = np.array(elements)

# Generate a 2-D array with 8 rows, each row containing 3 random numbers.
from numpy import random

x = random.rand(8, 3)
print(x.shape)
# What is its size? - 24
# Shape? - (8, 3)
# Print an np ones array with a shape (3, 3) with dtype=float. 
y = np.ones((3,3), dtype=int)
print(y.size)
# What is its size? - 9
# Print an np ones array with a shape (3, 3) with dtype=int. 
# What is its size? - 9
# Do you see any difference between these two arrays? - the int one does not have the decimal point for the values
# Print a 2D np array of size 20 comprised of random floats. (Several solutions!)
randArray = random.rand(2, 20)
print(randArray)
