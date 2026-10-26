def getIntegers(myList):
    integers=[i for i in myList if isinstance(i, int)]
    return integers

def test1():
  l1 = [x * .5 for x in range(20)]
  assert getIntegers(l1) == [i for i in range(10)]
  l2 = [x /3 for x in range(12)] 
  assert getIntegers(l2) == [i for i in range(4)]     