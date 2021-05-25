import numpy as np
import sys
py_array = [1, 2, 3, 4, 5, 6, 7]
py_array_size = sys.getsizeof(1) * len(py_array)
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7])
numpy_array_size = numpy_array.itemsize * numpy_array.size
sys.stdout.write(str(numpy_array_size))
sys.stdout.write(str(py_array_size))