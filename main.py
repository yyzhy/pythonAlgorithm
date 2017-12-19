import sort
import numpy as np
import time
a = 999
numarray = np.random.randint(10000, size = a)
num = numarray.tolist()
start1 = time.clock()
sort.quicksort(num, 0, a-1)
end1 = time.clock()


start2 = time.clock()
sort.quicksortr(num, 0, a-1)
end2 = time.clock()

print("\n01 quicksort use " + str(end1-start1) + "s.")
print("02 quicksortr use " + str(end2-start2) + "s.\n")
sort.printnum()