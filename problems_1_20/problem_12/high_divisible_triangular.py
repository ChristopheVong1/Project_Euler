def triangular_number(n):
    """
    Calculate the nth triangular number
    Arg: n(int), number of the triangular number
    Return: The nth triangular number
    """

    # Formula to calculate triangular number
    return n*(n+1)/2

def prime_factors(n):
    """
    Find every prime number that factor and their exponent
    Arg: n(int): The number to test
    Return: The dictionary with factors and the number of times or exponent
    """

    # Initialization of the dictionary, factors and exponents
    factors = {}

    # Handle even numbers
    while n % 2 == 0:
        # factors[2] meant looking for value for key=2. Fetch the current count of 2 (or give 0 if 2 isn't a key yet), then increment the count if even
        factors[2] = factors.get(2, 0) + 1
        # Divide by 2 until it is no longer even
        n = n // 2

    # Check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        # If i is a divisor of n (so a prime factor)
        while n % i == 0:
            # Creation of key i for the dictionnary and increment by 1
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        # Increment to skip even numbers
        i += 2
    
    # If remaining n is a prime > 2
    if n > 2:
        factors[n] = 1
    
    # Return the dictionary of factors
    return factors

def divisor_count(number):
    """
    Calculate the number of divisor using prime factorization
    Arg: number(int): Number to test
    Return: Number of divisor
    """
    
    # Edge case for number=1
    if number==1:
        return 1
    
    # Find every prime factors for number and exponent
    factors = prime_factors(number)
    
    # Initialization of count
    divisor_count=1

    # Formula: Divisor count=(a+1)*(b+1)*(c+1)*... with a,b,c, ... being exponent
    for exponent in factors.values():
        divisor_count*=(exponent+1)

    # Return the result
    return divisor_count

def high_div_triangular_number(target_divisor):
    """
    Find the value of the first triangle number to have over divisors
    Arg: divisor(int): Number of divisors to target
    Return: The first triangle number to have the target number of divisors
    """
    
    # Initialization of number of triangle number
    n=1

    # Iteration through every triangle number
    while True:
        # Calculation of triangular number
        test_number=triangular_number(n)
        # Check divisor count and compare with target
        if divisor_count(test_number)>target_divisor:
            break
        n+=1
    
    # Return the first triangle number that manage to break the while loop
    return triangular_number(n)

print(high_div_triangular_number(5))
print(high_div_triangular_number(500))
