import numpy as np
import sys
import time

py_array = [1, 2, 3, 4, 5, 6, 7]
py_array_size = sys.getsizeof(1) * len(py_array)
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7])
numpy_array_size = numpy_array.itemsize * numpy_array.size
sys.stdout.write(str(numpy_array_size))
print('\n')
sys.stdout.write(str(py_array_size))

print(np.__version__)

# Showing speed
# size of arrays and lists
size = 1000000  
 
# declaring lists
list1 = range(size)
list2 = range(size)
 
# declaring arrays
array1 = numpy.arange(size)  
array2 = numpy.arange(size)
 
# list
initialTime = time.time()
resultantList = [(a * b) for a, b in zip(list1, list2)]
 
# calculating execution time
print("Time taken by Lists :", 
      (time.time() - initialTime),
      "seconds")
 
# NumPy array
initialTime = time.time()
resultantArray = array1 * array2
 
# calculating execution time 
print("Time taken by NumPy Arrays :",
      (time.time() - initialTime),
      "seconds")
