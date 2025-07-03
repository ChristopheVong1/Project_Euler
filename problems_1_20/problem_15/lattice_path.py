def factorial(n):
    """
    Calculate factorial n
    Arg: n(int): Number to use for factorial
    Return: Factorial n
    """

    # Initialization of result
    result=1

    # Iteration for each value from 1 to n
    for i in range(1,n+1):
        result*=i

    # Return factorial n
    return result

def lattice_path(grid_size):
    """
    Calculate the number of lattice path by calculating the central binomial coefficient
    Arg: grid_size (int): Size of the grid
    Return: Number of possible path
    """

    # Use formula with central binomial coefficient to calculate the number of path
    return factorial(2*grid_size)//((factorial(grid_size))**2)

# Expected answer = 6
print(lattice_path(2))
# Expected answer = 137_846_528_820
print(lattice_path(20))