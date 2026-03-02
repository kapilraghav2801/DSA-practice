def add_logging(original_function):
    def wrapper():
        print("Function is about to run")
        result = original_function()
        print("Function Finished")
        return result
    return wrapper
# WITHOUT decorator
def say_hello():
    return "Hello"
print(say_hello())

# WITH decorator (the @ symbol)
@add_logging
def say_hi():
    return "Ho"


print(say_hi())