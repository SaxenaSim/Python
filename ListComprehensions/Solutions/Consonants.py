inputString="Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuks yams"
vowels = ['a','e','i','o','u',' ']
consonants=[x for x in inputString if x not in vowels]
print(consonants)