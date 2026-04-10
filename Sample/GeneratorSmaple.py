# What is Generator

# A generator is a special type of iterator that is created using a function with yeild

# Simple Genarator

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# Generator with Loop

def count_up_to(n):
    for i in range(1, n+1):
        yield i

for num in count_up_to(10):
    print(num)

