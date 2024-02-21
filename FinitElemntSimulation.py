from fenics import *
import matplotlib.pyplot as plt

# Define the mesh and function space
L = 1.0  # Length of the rod
nx = 10  # Number of elements
mesh = IntervalMesh(nx, 0, L)
V = FunctionSpace(mesh, 'P', 1)

# Define boundary conditions
def boundary(x, on_boundary):
    return on_boundary

bc_left = DirichletBC(V, Constant(100), 'near(x[0], 0)')
bc_right = DirichletBC(V, Constant(0), 'near(x[0], 1)')
bcs = [bc_left, bc_right]

# Define the problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(0)  # No heat source
a = dot(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bcs)

# Plot the solution
plot(u)
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('1D Heat Conduction')
plt.show()
