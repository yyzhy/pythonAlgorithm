import random
x = 0
y = 0
def quickSort(num, l, r):
    global x
    x += 1
    print(str(x) + ": hello quicksort().")
    if l >= r:
        return
    flag = l
    for i in range(l+1, r+1):
        print("x...")
        if num[flag] > num[i]:
            tmp = num[i]
            del num[i]
            num.insert(flag, tmp)
            flag = flag + 1
    quickSort(num, l, flag - 1)
    quickSort(num, flag + 1, r)

def quickSortr(num, begin, end):
    global y
    y += 1
    print(str(y) + ": hello quicksortr().")
    if begin >= end:
        return
    k = random.randint(begin, end)
    tmp1 = num[begin]
    num[begin] = num[k]
    num[k] = tmp1
    flag = begin
    for i in range(begin+1, end+1):
        print("y...")
        if num[flag] > num[i]:
            tmp2 = num[i]
            del num[i]
            num.insert(flag, tmp2)
            flag = flag + 1
    quickSortr(num, begin, flag - 1)
    quickSortr(num, flag + 1, end)

def printnum():
    global x, y
    print("01 quickSort has done " + str(x) + " times.")
    print("02 quickSortr has done " + str(y) + " times.")
