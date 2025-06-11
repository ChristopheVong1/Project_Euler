import math

def is_prime(n):
    """
    Check if a number is a prime by testing the divisibility with lower than n value
    Arg: n(int): An integer to test
    Return: True or False if the number is prime or not
    """

    # Edge case for n=1 (not prime by default)
    if n<=1:
        return False
    # Edge case for n=2 (prime by default)
    elif n==2:
        return True
    # Every even number are not prime
    elif n%2==0:
        return False

    else:
        # For optimization, no need to test number higher than sqrt(n)
        for i in range(3,int(math.sqrt(n))+1,2):
            # Check the divisibility with every number i
            if n%i==0:
                return False
        # If no number i found, n is a prime number
        return True

def consecutive_prime(a,b):
    """
    Find the number of prime number for a pair (a,b) using quadratic forms
    Args: a(int), b(int): Integer to create the formula n2+an+b
    Return: The highest n that manages to produce the maximum number 
    of primes for consecutive values of n starting from n=0
    """

    # Initialization
    n=0

    # Iteration until condition fails
    while is_prime(n**2+a*n+b):
        n+=1

    # Return the final result
    return n

def quadratic_primes(A,B):
    """
    Find the pair between limit given for a and b that produce the highest
    consecutive number of prime numbers
    Args: A(int) and B(int): Limit for a and b: n2+an+b where ∣a∣<A and ∣b∣≤B
    Return: The product of the pair (a,b) that gives the best result
    """

    # Initialization
    a,b=0,0
    best_consecutive_prime=consecutive_prime(a,b)

    for i in range (-A+1,A,1):
        for j in range (-B,B+1,1):
            # Check if the current combination i,j produce longer consecutive prime number
            if consecutive_prime(i,j)>best_consecutive_prime:
                a,b=i,j
                best_consecutive_prime=consecutive_prime(i,j)
    
    # Return the product a and b that produce the best result
    return a*b

# Expected answer: -59231 for (a=-61 and b=971)
print(quadratic_primes(1000,1000))