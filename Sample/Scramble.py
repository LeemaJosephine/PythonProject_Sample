# # import random
# #
# # words = ["python", "java", "automation", "selenium"]
# # original_word = random.choice(words)
# #
# # scrambled = ''.join(random.sample(original_word, len(original_word)))
# #
# # print("Scrambled word:", scrambled)
# #
# # guess = input("Guess the word: ")
# #
# # if guess == original_word:
# #     print("Correct!")
# # else:
# #     print("Wrong. Correct word was:", original_word)
#
#
# numbers = [10,8, 6, 4, 2]
#
#
# even = [a**2 for a in numbers if(lambda n: n%2 == 0)(a)]
# print(even)
#
# from functools import reduce
#
# numbers = [2, 4, 6, 1, 3, 5]
#
# results = reduce (lambda a,b: a*b, numbers)
# print(results)
#
#
# people = [
#     {"name": "Asha", "age": 25},
#     {"name": "John", "age": 16},
#     {"name": "Kumar", "age": 30},
#     {"name": "Rita", "age": 14}
# ]
#
# adults = list(filter(lambda p: p["age"] >= 18, people))
# adults_names = list(map(lambda p: p["name"], adults))
# print(adults_names)
#
# fib_n = lambda n: n if n <= 1 else fib_n(n-1) + fib_n(n-2)
#
#
# n_terms = 10
# series_lambda = [fib_n(i) for i in range(n_terms)]
# print(f"Fibonacci series using recursive lambda: {series_lambda}")
#
# from datetime import datetime
#
# extract_date = lambda d : (d.year, d.month, d.day)
# dt = datetime(2025, 12, 15)
#
# print(extract_date(dt))
#
# is_number = lambda s: s.isdigit()
#
# print(is_number("123"))
# print(is_number("12a"))
# print(is_number("45.6"))

# From a list of words choose and scramble and display
# If user guesses correctly then ask for input switch to next scrambled word
# import random
# Lst_str=["python", "javascript", "automation", "pytest", "guvi", "selenium"]
# Loop_var=0
# while Loop_var <= 5:
#     Scrambled_Word=list(Lst_str[Loop_var])
#     random.shuffle(Scrambled_Word)
#     Scrambled_Word=''.join(Scrambled_Word)
#     print(Scrambled_Word)
#     User_guess = input("Enter Your Guess: ")
#     if User_guess != Lst_str[Loop_var]:
#         print("Good guess. But Try again")
#         continue
#     elif User_guess == Lst_str[Loop_var]:
#         Usr_choice=input("Wow. What a match!!Do you want to continue Guessing Y/N: ")
#         if Usr_choice == 'Y' or Usr_choice == 'y':
#             Loop_var +=1
#             continue
#         else:
#             break

def fibonacci(iteration_count):
    list = [0, 1]
    any(map(lambda _: list.append(sum(list[-2:])), range(2, iteration_count)))
    return list[:iteration_count]

print(fibonacci(10))