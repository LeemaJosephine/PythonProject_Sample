# What is Iterator

# An Iterator is an Object that allows you to traverse a collection of elements one at a time.

# _iter_() and _next_() methods

# Example

numbers = [10,20,30]

# Convert list to iterator

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # StopIteration error

# Custom Iterator

class CoutUP:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self  # This object itself is an iterator

    def __next__(self):
        if self.current <= self.max:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

counter =CoutUP(3)

for num in counter:
    print(num)