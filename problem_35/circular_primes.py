def is_prime(n):
    """
    Check if a number is prime.
    Arg: n(int): Integer to test
    Return: Boolean depending on the test
    """
    # Edge case for n<=1
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Check divisibility with 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check divisibility from 5 up to sqrt(n)
    i = 5
    while i * i <= n:
        # Check divisibility
        if n % i == 0:
            return False
        # Skip odd numbers
        i += 2
    # If not divisors found, the number is prime
    return True

def rotations(n):
    """Generate a list of number using rotations of number's digit"""
    # str() for digit access
    s=str(n)
    rotation_list=[]
    for i in range(len(s)):
        rotation_list.append(int(s[i:]+s[:i]))
    return rotation_list

def is_circular_prime(n):
    """Check if a number is a circular prime but testing every number with rotations"""
    if not is_prime(n):
        return False
    for rotation in rotations(n):
        if not is_prime(rotation):
            return False
    return True

def circular_primes(max):
    """
    Find the number of circular prime below max
    Args: max(int): Maximum bound for numbers to test
    Return: int: The number of circular prime
    """
    # Initialization
    circular_list=[]

    # Edge case for single digit prime
    for n in [2, 3, 5, 7]:
        if n < max:
            circular_list.append(n)

    # Iteration to test every number until max (skip odd number)
    for n in range(11,max,2):
        # str() for digit access
        s=str(n)
        # skip number if s contain digit 024568
        if any(d in s for d in "024568"):
            continue
        # Check circular prime or not
        if is_circular_prime(n):
            circular_list.append(n)

    # Return the number of circular prime
    return len(circular_list)

# Expected answer: 55
print(circular_primes(1000000))