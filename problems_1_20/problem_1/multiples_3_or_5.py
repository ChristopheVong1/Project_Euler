def multiples_list(max_number):

    """
    Calculates the sum of all natural numbers below a given limit that are multiples of 3 or 5.

    Args: max_number (int): Upper limit (exclusive) for finding multiples

    Returns: int: Sum of all multiples of 3 or 5 below max_number
    """

    multiples_list=[]

    for i in range (max_number):
        # Check if 'i' is a multiple of 3 or 5 using modulo arithmetic
        if i%3==0 or i%5==0:
            # Append valid multiples to the list
            multiples_list.append(i)

    # Return the sum of all collected multiples
    return sum(multiples_list)

# Test cases with descriptive output

# Expected output: 23
print(multiples_list(10))
# Output to find
print(multiples_list(1000))