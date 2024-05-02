# Filter negative numbers

numbers = [1, 2, -4, 7, -8, 9, -11, 12, 15, 16, -7]

# Filter negative numbers using list comprehension
filtered_numbers = [num for num in numbers if num >= 0]

# Print the result
print("All Numbers:", numbers)
print("---------------")
print("Filtered Numbers (non-negative):", filtered_numbers)