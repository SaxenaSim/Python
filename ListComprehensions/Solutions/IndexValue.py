myList = ['hi',4,8.99,'apple',('t,b','n')]
result = [(myList.index(x),x) for x in myList]
print(result)