def getIntegers(myList):
    integers=[i for i in myList if is.integer(i)]
    return integers

l1 = [x * .5 for x in range(20)]
print(getIntegers(l1) == [i for i in range(10)])
l2 = [x /3 for x in range(12)]
print(getIntegers(l2) == [i for i in range(4)])