# Write a Python decorator uppercase that converts the return value of a function to uppercase.

def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))