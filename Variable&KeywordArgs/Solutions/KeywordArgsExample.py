def intro(**data):
    print("DataType of Argument:",type(data))
    for key,value in data.items():
        print("{},{}",key,value)

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
