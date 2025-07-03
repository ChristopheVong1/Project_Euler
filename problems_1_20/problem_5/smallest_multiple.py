def smallest_multiples(max_number):
    """
    Finds the smallest positive number that is evenly divisible by all integers from 1 to max_number
    Args: max_number(int): Upper bound of the divisor range (inclusive)
    Returns: int: The smallest number divisible by all integers in [1, max_number]
    """

    # Start checking from the largest possible divisor
    solution=max_number

    # Continue searching until solution is found
    while True:
        # Assume current solution is valid until proven otherwise
        divisible=True

        # Check divisibility for all numbers in range
        for i in range (1,max_number+1, 1):
            # If any division fails
            if solution%i!=0:
                divisible=False
                break

        if divisible:
            # Return when all divisions succeed
            return solution
        else:
            # Try next candidate number
            solution+=1

print(smallest_multiples(20))