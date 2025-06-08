from itertools import permutations

def lexicographic_permutations():
    """
    Find the 1_000_000th lexicographic permutations using permutations() from itertools
    Args: None
    Return: The 1_000_000th lexicographic permutations
    """

    # List of number for lexicographic permutations
    digits="0123456789"

    # Create an iterator object for permutations
    permutations_list=permutations(digits)

    # Iterations until we reach the 1_000_000th object
    for i in range(1000000):
        # next() allow us to go to the next permutation in the sequence
        solution=next(permutations_list)

    # Return the result after conversion of the data into correct format
    return "".join(solution)

# Expected answer: 2_783_915_460
print(lexicographic_permutations())