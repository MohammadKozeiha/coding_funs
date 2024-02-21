'''
implemet the function in python solve(weight_1, weight_2, weight_3) that takes 3 integers.
these values represent the weight of the packages available on the convoyer belts with
respective index 0, 1, 2. when the convoyer belt is empty the value is 0.
the function shoould return the index of the convoyer belt that has the haviest package.
for exapmle if the values for weight_0, weight_1, weight_2 are 85,100,90, then the expected answer is 1. in case of equality , any correct answer is accepted? the function will be called successivly until the convoyer is emty


'''

def solve(weight_1, weight_2, weight_3):
    weights = [weight_1, weight_2, weight_3]
    max_weight = max(weights)
    return weights.index(max_weight)

# Example usage:
weight_0 = 85
weight_1 = 100
weight_2 = 90

result = solve(weight_0, weight_1, weight_2)
print(f"The heaviest package is on convoyer belt {result}")