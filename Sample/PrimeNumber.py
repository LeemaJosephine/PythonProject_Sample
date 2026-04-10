numbers = [2,3,5,7,10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []

for num in numbers:
    if num > 1:                     # prime numbers must be greater than 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:         # if divisible by any number
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime Numbers List:", prime_numbers)
print("Count of Prime Numbers:", len(prime_numbers))
