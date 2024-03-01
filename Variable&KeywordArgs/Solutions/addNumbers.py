def addNumbers(*args):
    total=0
    for num in args:
        total+=num
    return total

print(addNumbers(10,1,3,5,7,8,4,5))
print(addNumbers(43,65,12,87))
print(addNumbers(2,5))
