def calculator_decorator(func):
    def wrapper(a,b):
        print("Calculation Started")
        func(a,b)
        print("Calculation Finished")
    return wrapper

@calculator_decorator
def add(a, b):
    print(a + b)

@calculator_decorator
def subtract(a, b):
    print(a - b)

add(1, 2)
subtract(1, 2)