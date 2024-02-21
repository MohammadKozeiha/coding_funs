def calculate_average(arr):
    return sum(arr) / len(arr) if arr else None

# Test the function
my_array = [1, 2, 3, 4, 5]
print("Average of the array:", calculate_average(my_array))  # Output: Average of the array: 3.0
