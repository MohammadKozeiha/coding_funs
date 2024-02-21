def is_on_even(table, value):
    if len(table) == 0:
        return False
    index = table.index(value) if value in table else -1
    return index % 2 == 0 and index != -1

# Test the function
table = [1, 2, 3, 4, 5]
value = 3
print(is_on_even(table, value))  # Output: False
