import sort
import numpy as np
import time
import find

a = 99
numarray = np.random.randint(10000, size = a)
num = numarray.tolist()
start1 = time.clock()
sort.quickSort(num, 0, a-1)
end1 = time.clock()


start2 = time.clock()
sort.quickSortr(num, 0, a-1)
end2 = time.clock()

print("01 quicksort use " + str(end1-start1) + "s.")
print("02 quicksortr use " + str(end2-start2) + "s.")
sort.printnum()

list = [1,2,3,4,5,6,7,8]
item = 6
res = find.binFind(list, item)
if res == False:
    print("item " + str(item) + " is not in the list.")
else:
    print("item " + str(item) + " is in the list.")