numbers = [1,10, 501, 22, 37, 100, 999, 87, 351,19]

happy_numbers = []

for num in numbers:
    seen = set()
    temp = num

    while temp != 1 and temp not in seen:
        seen.add(temp)
        temp = sum(int(digit) ** 2 for digit in str(temp))

    if temp == 1:
        happy_numbers.append(num)

print("Happy Numbers List:", happy_numbers)
print("Count of Happy Numbers: ", len(happy_numbers))



