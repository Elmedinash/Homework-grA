numbers = [1, 2, 3, 4, 5]

# Using **list comprehension**:
# Return a list of squares of even numbers only
squered = [n**2 for n in numbers if n % 2 == 0]

print(squered)
