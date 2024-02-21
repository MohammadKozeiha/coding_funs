import numpy as np

def reshape(line, n):
    # Remove spaces from the input line
    line = line.replace(" ", "")

    # Calculate the number of chunks needed
    num_chunks = (len(line) + n - 1) // n

    # Initialize an empty numpy array to store the chunks
    result = np.empty((num_chunks, 1), dtype='U'+str(n))

    # Iterate over the characters in the input line
    for i in range(num_chunks):
        # Get the chunk of length n
        chunk = line[i * n : (i + 1) * n]

        # Assign the chunk to the numpy array
        result[i, 0] = chunk

    return result

# Test the function
line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
n = 10
result = reshape(line, n)

# Print the result
print(result)
