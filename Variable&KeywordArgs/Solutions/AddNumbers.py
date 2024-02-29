def addNum(*args):
    total=0
    for num in args:
        total+=num
    return total

print(addNum(10,1,3,5,7,8,4,5))
print(addNum(43,65,12,87))
print(addNum(2,5))
