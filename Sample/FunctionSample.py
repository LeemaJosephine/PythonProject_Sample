#Normal function
def ford_motors(string1):
    print("Ford motor method", string1)

def tata_motors(string2):
    print("This method returns value", string2)
    return string2

ford_motors("Car2")  # No return
print(tata_motors("Car1"))  # when the method returns something

# closure function

def outer_function(msg):
    print("Welcome to outer function")
    def inner_function():
        print("Inner function", msg)
    return inner_function

my_closure = outer_function("I'm from closure function")
my_closure()

