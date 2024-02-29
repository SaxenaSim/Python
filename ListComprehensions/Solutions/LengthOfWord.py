sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'

words = sentence.split()

result = [word for word in words if len(word) >=4]
print(result)