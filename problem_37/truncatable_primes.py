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

def truncatable_left(n):
    """
    Return a new number by removing the first digit (left)
    Arg: n(int): An integer with at least 2 digit
    Return: int: The truncated number (from the left)
    """
    # str() conversion to get digit access
    digits=str(n)
    # Edge case for single digit number
    if len(digits)<2:
        return None
    # Return the value except the first digit 
    return int(digits[1:])

def truncatable_right(n):
    """
    Return a new number by removing the last digit (right)
    Arg: n(int): An integer with at least 2 digit
    Return: int: The truncated number (from the right)
    """
    # str() conversion to get digit access
    digits=str(n)
    # Edge case for single digit number
    if len(digits)<2:
        return None
    # Return the value except the first digit 
    return int(digits[:-1])

def is_truncatable_prime(n):
    """
    Check if a number n is prime and every truncatable version are also primes
    Arg: n(int): An integer of at least 2 digit
    Return: boolean: Depending of yes or no
    """
    # str() conversion for digit access
    digits=str(n)
    # Check if there are at least 2 digits
    if len(digits)<2:
        return False
    # Case if n is not a prime number
    if not is_prime(n):
        return False
    
    # Initialization to check every truncatable number from left
    left_trunc=n
    # Recursive to check every number by removing the first digit every time
    while left_trunc>=10:
        left_trunc=truncatable_left(left_trunc)
        if not is_prime(left_trunc):
            return False

    # Initialization to check every truncatable number from right
    right_trunc=n
    # Recursive to check every number by removing the first digit every time
    while right_trunc>=10:
        right_trunc=truncatable_right(right_trunc)
        if not is_prime(right_trunc):
            return False

    # Return True if everything works
    return True

def truncatable_primes():
    """
    Find every number that are truncatable primes and return the sum
    Arg: None
    Return: The sum of every number that fulfills the case (there are only 11 numbers)
    """
    # Initialization of the final list
    truncatable_list=[]
    # Starting number
    n=11

    # Iteration until we reach 11 numbers
    while len(truncatable_list)<11:
        digits=str(n)
        if any(d in digits[1:] for d in '024568'):
            n+=2
            continue
        else:
            if is_truncatable_prime(n):
                truncatable_list.append(n)
        n+=2

    # Return the sum of the final list
    return sum(truncatable_list)

# Expected answer: 748_317
print(truncatable_primes())