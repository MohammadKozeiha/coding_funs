import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def finite_element_method(num_elements):
    # Define the domain
    length = 1.0  # Length of the rod
    num_nodes = num_elements + 1
    nodes = np.linspace(0, length, num_nodes)

    # Define the conductivity (thermal conductivity) of the material
    conductivity = 1.0

    # Define the boundary conditions
    temperature_left = 100.0
    temperature_right = 0.0

    # Define the system matrix and vector
    A = np.zeros((num_nodes, num_nodes))
    b = np.zeros(num_nodes)

    # Assemble the system matrix and vector
    for i in range(num_elements):
        h = nodes[i + 1] - nodes[i]
        k = conductivity / h

        A[i, i] += k
        A[i, i + 1] -= k
        A[i + 1, i] -= k
        A[i + 1, i + 1] += k

    # Apply boundary conditions
    A[0, 0] = 1.0
    A[-1, -1] = 1.0
    b[0] = temperature_left
    b[-1] = temperature_right

    # Solve the system
    temperature_distribution = solve(A, b)

    return nodes, temperature_distribution

def plot_temperature_distribution(nodes, temperature_distribution):
    plt.plot(nodes, temperature_distribution, marker='o')
    plt.title('Temperature Distribution')
    plt.xlabel('Position')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.show()

# Example usage
num_elements = 10
nodes, temperature_distribution = finite_element_method(num_elements)
plot_temperature_distribution(nodes, temperature_distribution)