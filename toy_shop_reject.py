'''you work in a factory and your objective is to write a function that will dispatch
the packages to the correct stack,
according to their mass and volume. a pacakge is bulky is its
volume is >= 1000000 or when one ot its dimensions is >= 150 cm
a package is heavy if it is >= 20 kg
you should dispach packages as the following stacks:
STANDARD :(not bulky or havy
special : packages are either heavy or bulky
REJECTED: packages are both heavy and bulky
implement the function solve(widh, height, length, mass)
 units are centimeter aand kilo formass. the function should return a string :
 the name of the stack where the package should go in python '''
def solve(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in (width, height, length))
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example usage:
width = 120
height = 80
length = 130
mass = 15

result = solve(width, height, length, mass)
print(f"The package should go in the {result} stack.")
