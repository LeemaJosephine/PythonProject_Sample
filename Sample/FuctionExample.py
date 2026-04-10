#Postional Arguments
def add(a,b):
    print(a+b)

add(5,10)   #Passing values

#Keywords Argument

def greet(name,msg):
    print(name,msg)

greet(msg="Hello", name="Ben")

#Default Argument

def greet1(nam,msg1="Welcome"):
    print(msg1,nam)

greet1("Ben")

# Arbitrary Arguments

#*args (Non-keyword)

def total(*numbers):
   print(numbers)

total("Hello","User",123)

#**kargs (Keywords)

def details(**info):
    print(info)

details(a=1,b=2,c=3)


# Inner Function

def outer():
    print("Outer")
    def inner():
        print("inner")  #Used for logical grouping
    inner()  # call inside the outer

outer()

def calculator(a,b):
    print("Welcome to calculator App")

    def add():
        print(a+b)
    def subtract():
        print(a-b)
    def multiply():
        print(a*b)

    add()
    subtract()
    multiply()

calculator(1,2)

#Return Statement

def addition(a,b):
    c = a+b
    return c

result = addition(1,2)
print(result)

# Function Closure

def outer2(x):
    def inner2():
        print(x)
    return inner2

closure_func = outer2(10)
closure_func()

# Recursive Function  - Function that calls itself

def factorial(n):
   if n == 1:
       return 1
   return n * factorial(n - 1)

print(factorial(5))
