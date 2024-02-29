class Square:
    def __init__(self, side_length):
        print("Inside init!")
        self.side_length = side_length
        print(self.side_length)

sq = Square(1)