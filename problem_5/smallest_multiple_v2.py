# Import GCD function from math module
from math import gcd

def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers using 
    their GCD.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: LCM of a and b
        
    Formula:
        LCM(a, b) = (a * b) // GCD(a, b)
    """

    # Using standard LCM formula
    return a * b // gcd(a, b)

def smallest_multiple(max_num):
    """
    Find the smallest number divisible by all integers from 1 to 
    max_num.
    
    Args:
        max_num (int): Upper bound of the range (inclusive)
        
    Returns:
        int: The smallest positive divisible number
        
    Approach:
        - Iteratively computes LCM of the running result with each 
        number in range
        - Efficiently builds the solution using mathematical 
        properties of LCM
    """
    result = 1
    for i in range(1, max_num + 1):
        result = lcm(result, i)
    return result

print(smallest_multiple(20))  # Output: 232792560