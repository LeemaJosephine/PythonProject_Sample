def first_non_repeating(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i
    return None

# Example
numbers = [4, 5, 1, 2, 0,4]
result = first_non_repeating(numbers)

print("First non-repeating element:", result)
