def cycle_length(d):
    """
    Find the cycle length of a number d
    Args: d(int): An integer from 1 to 1000
    Return: The cycle length if d creates a cycle
    """

    # Edge case for d=1
    if d == 1:
        # 1/1 = 1.0 (no cycle)
        return 0  
    
    # Initialization of list of remainders
    remainders = []  # Stores all remainders in order
    remainder = 1    # Start with numerator = 1

    # We make long division until the remainder is 0 or it repeats    
    while True:
        # Carry over the remainder so that we divide it (retenue)
        remainder *= 10
        # Compute the quotient
        quotient = remainder // d
        # Compute the new remainder
        remainder = remainder - (d * quotient)
        
        # No cycle (terminating decimal)
        if remainder == 0:
            return 0
        
        # If remainder is already in the full list, it will repeats indefinitely
        if remainder in remainders:
            # The cycle length = distance between repeats
            return len(remainders) - remainders.index(remainder)
        
        # If no repeat, we add to the list of remainder and reoeat the division
        remainders.append(remainder)

def reciprocal_cycles(n):
    """
    Find a value d<n with the longest recurring cycle
    Args: n(int): The maximum value
    Return: The value d with the longest recurring cycle
    """

    length_list=[]

    for d in range(1,n+1):
        length_list.append(cycle_length(d))
    
    max_length=max(length_list)
    return length_list.index(max_length)

# Expected answer: 982
print(reciprocal_cycles(1000))