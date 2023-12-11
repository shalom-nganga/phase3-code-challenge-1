def exactly_two_positive(a, b, c):
    # Count the number of positive numbers
    positive_count = sum(num > 0 for num in (a, b, c))
    
    # Check if exactly two numbers are positive
    return positive_count == 2

# Test cases
print(exactly_two_positive(2, 4, -3))   # True
print(exactly_two_positive(-4, 6, 8))   # True
print(exactly_two_positive(4, -6, 9))   # True
print(exactly_two_positive(-4, 6, 0))   # False
print(exactly_two_positive(4, 6, 10))   # False
print(exactly_two_positive(-14, -3, -4))  # False
