def number_spiral_diagonal(k):
    """
    Compute the sum of the numbers on the diagonals of a spiral (Euler problem 28)
    Args: k(int): The maximum size of the matrix spiral, for a matrix of 1001*1001, k=500
    Return: int: The sum of the numbers on the diagonals
    """

    # Initialization because the center is always 1
    diagonal_sum=1

    # Iteration from the second layer to the k-th layer
    for i in range(1,k+1,1):
        # See description for math
        diagonal_sum+=16*(i**2)+4*i+4

    return diagonal_sum

# Expected answer: 66917001
print(number_spiral_diagonal(500))