sentence = "In 1984 there were 13 instances of a protest with over 1000 people attending."
words=sentence.split()
result=[num for num in words if num.isnumeric()]
print(result)