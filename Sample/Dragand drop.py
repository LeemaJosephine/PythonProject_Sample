#1.to find two list contains even number list and odd number list
list = [10,501,22,37,100,999,87,351] #list of given numbers
#creating empty list to store even numbers and odd numbers
even_numbers = []
odd_numbers = []
#loop through each numbers in the list
for numbers in list:
    #check if the number is even
    if numbers %2 == 0:
        even_numbers.append(numbers)
    else:
        odd_numbers.append(numbers)
        #print the result
print("Even numbers:", even_numbers)
print("odd numbers:", odd_numbers)

#2.To count prime numbers and print list of prime numbers
integers = [10,501,22,37,100,999,87,351]
def prime(num):
    if num<=1:
        return False
    else:
        for i in range(2, int(num*0.5)+1): #iterating to find a prime number
            if num % i == 0:
                return False
        return True
prime_numbers= []
for n in integers:
    if prime(n):
        prime_numbers.append(n)
        print("Prime numbers:", prime_numbers)
        print("count of prime numbers:", len(prime_numbers))

#3.TO finding happy numbers
def hppy_numbers(n): #functionn ti find a hppy numbers
    seen = set()
    while n!=1 and n not in seen:
        seen.add(n)
        sum_square = sum(int(digit)**2 for digit in str(n))
        n = sum_square
    return n == 1
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_count=0 #To count a happy numbers in a given list
happy_list=[]
for num in numbers:
        if hppy_numbers(num):
            happy_count += 1
            happy_list.append(num)
            print("Happy numbers are ", happy_list)
            print("the count of happy numbers:", happy_count)

#4.To find the sum of the first and last digit of an integer

number = int(input("Enter the number: "))
last_digit = number%10
first_digit = number
while first_digit>10:
    first_digit //= 10
result = first_digit + last_digit
print("sum of the first and last digit is ", result)

#5.Ways to make 10rs.coin using rs.1, rs.2, rs.5 and rs.10 coins
print("the way of to make 10rs coin")
count = 0
for c1 in range(2):
    for c2 in range(3):
        for c5 in range(6):
            for c10 in range(11):
                total = c1*10 + c2*5 + c5*2 + c10*1
                if total == 10:
                    count += 1
                    print("1rs:{c1}, 2rs:{c2}, 3rs:{c5}, 4rs:{c10}".format(**locals()))
from distutils.spawn import find_executable

#6. Find the duplicates in given list
number1 = [44, 55,44, 20, 22, 33]
number2 = [4, 5,4, 20, 2, 3,5]
number3 = [20,30,40,20,30]
duplicates = set(number1) & set(number2) & set(number3) #using intersection for across all the list of numbers
print("duplicates in the all 3 lists:", duplicates)

def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print(duplicates)

find_duplicates(number1)
find_duplicates(number2)
find_duplicates(number3)



#7.find the first non-repeating elements
numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#to find the first non-repeating element
first_non_repeat = None
for num in numbers:
    if numbers.count(num) == 1:
        first_non_repeat = num
        break
print("First non-repeating element:", first_non_repeat)

#8.To find the minimum element in a rated and sorted list
nums = [23, 45, 56, 11, 99, 77]
print("Minimum element in a given list", min(nums)) #using min function to find the minimum element

#9.To find a triplet in a given list whose sum is equal to 59
nums = [10, 20, 30, 9]
value = 59
found = False
#loop starts through all triplets
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k] == value:
                print("triplet of the list is" ,nums[i], nums[j], nums[k])
                found = True
if not found:
    print("the list isn't found")

#10.In a given list to find a sub-list whose sum is zero
def sub_list(nums):
    prefix_sum = {}
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        #sub-list from index 0 to i has sum = 0
        if current_sum == 0:
            return (0, i)

        #if current_sum already occurred, sub-list is between previous index+1 to i
        if current_sum in prefix_sum:
            return (prefix_sum[current_sum] + 1, i)

        prefix_sum[current_sum] = i

    return None

arr = [4, 2, -3, 1, 6]
result = sub_list(arr)

if result:
    start, end = result
    print("Zero-sum sub-list found:", arr[start:end + 1])
else:
    print("No zero-sum sub-list found.")





#1.Person who have above 18 in the given list
people = [
    {"name": "john", "age": 30},
    {"name": "Aishu", "age": 16},
    {"name": "meera", "age": 28},
    {"name": "Meena", "age": 14}
]
# Filter people who are 18 or older
adults = filter(lambda person: person["age"] >= 18, people)
# Map the remaining people's names to a list
adult_names = list(map(lambda person: person["name"], adults))
print(adult_names)

#2.product of numbers in the list
from functools import reduce
numbers = [11,22,33,44]
# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)

#3.square of even numbers in the list
numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = [
    (lambda x: x * x)(n)
    for n in numbers
    if (lambda x: x % 2 == 0)(n)
]
print(squares_of_evens)

#4.Check if given string is number
is_number = lambda s: s.replace('.', '', 1).isdigit()
print(is_number("12.5"))
print(is_number("3.14"))
print(is_number("12.5.3"))

#5.to extract the day, year, month from a datetime object
from datetime import datetime
dates = [
    datetime(2023, 1, 10),
    datetime(2024, 6, 25),
    datetime(2025, 12, 5)
]
result = list(map(lambda d: (d.year, d.month, d.day), dates))
print(result)

#6.fibonacci series up to n terms
from functools import reduce
fibonacci = lambda n: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]],
    range(n - 2),
    [0, 1]
)[:n]

print(fibonacci(10))