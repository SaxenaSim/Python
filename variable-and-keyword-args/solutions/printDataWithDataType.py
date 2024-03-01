def data(**details):
    print("DataType of Argument:",type(details))
    for key,value in data.items():
        print("{},{}",key,value)

data(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
data(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
