class Employee:
    def __init__(self):
        self.name="Karan"
        self.salary=17383

    def __str__(self):
        return (f"Name = {self.name} Salary= {self.salary}")

e=Employee()
print(e)

# this function is used to return the string representation of the object.