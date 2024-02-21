def closest(ints):
    closest_positive = float('inf')
    closest_negative = float('-inf')

    for num in ints:
        if num == 0:
            return 0
        elif num > 0 and num < closest_positive:
            closest_positive = num
        elif num < 0 and num > closest_negative:
            closest_negative = num

    if abs(closest_positive) <= abs(closest_negative):
        return closest_positive
    else:
        return closest_negative

# Test the function
ints = [-3, 5, -5, 7, 2]
print(closest(ints))  # Output: 5
