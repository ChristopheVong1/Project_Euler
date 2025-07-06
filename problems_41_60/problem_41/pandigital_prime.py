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

def is_pandigital(s, n=None):
    """
    Check if a string (of a number) is pandigital (contain every digit 
    from 1 to n once)
    Arg: s(int): A string (that represent a number) to test
    n(int): The expected length
    Return: bool: A boolean depending if pandigital or not
    """

    # Assume n is the length of the string if not provided
    if n is None:
        n = len(s)  

    # The length must be exactly n and every char from 1-9 must be included
    return len(s) == n and set(s) == set(str(d) for d in range(1,n+1))

def pandigital_prime():
    """
    Find the biggest pandigital prime (see description for strategy)
    Arg: None
    Return: The biggest pandigital prime
    """

    # Initialization
    biggest_pan_prime=0

    # Iteration through every 7 digit number
    for i in range(7654321,1234567,-1):
        if is_pandigital(str(i)) and is_prime(i):
            biggest_pan_prime=i
            return biggest_pan_prime

    # Iteration through every 4 digit number
    for i in range(4321,1234,-1):
        if is_pandigital(i) and is_prime(i):
            biggest_pan_prime=i
            return biggest_pan_prime

    # Return the result
    return biggest_pan_prime

# Expected answer: 7_652_413
print(pandigital_prime())