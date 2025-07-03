def proper_divisors(n):
    """
    Find the proper divisors of n by testing every number below n
    Arg: n(int): An integer number
    Return: A set with every proper divisors of n
    """

    # Edge case for n=1
    if n == 1:
        return set()
    
    # Initialization
    divisors = set()

    # Iteration through every number from 2 to n
    for i in range(1, n):
        # Check divisors condition
        if n % i == 0:
            divisors.add(i)

    # Return the final list
    return divisors

def sum_proper_divisors(n):
    """
    Calculate the sum of proper divisors of integer n using the function proper_divisors
    Arg: n(int): An integer number
    Return: The sum of proper divisors of n
    """
    return sum(proper_divisors(n))

def is_abundant(n):
    """
    Check if the number n is abundant or not by checking the sum of proper divisors
    Arg: n(int): An integer number
    Return: Boolean True if abundant
    """
    return sum_proper_divisors(n) > n

def non_abundant_sum():
    """
    Calculate the sum of non abundant integer below n
    Arg: None
    Return: The sum of non abundant number
    """

    # Creation of the list of every abundant number between 1 and target_number
    abundant_numbers = [n for n in range(1, 28124) if is_abundant(n)]

    # Initialization of the set of the sum of every abundant number
    sums_of_abundants = set()

    # Iteration through every abundant numbers
    for i in range(len(abundant_numbers)):
        # Iteration through every abundant numbers starting from i to avoid redundancy
        for j in range(i, len(abundant_numbers)):
            # Compute the sum of 2 abundant numbers
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            # Break condition because the solution doesn't exist above 28123
            if sum_abundant > 28123:
                break
            # Addition of sum of two abundant
            sums_of_abundants.add(sum_abundant)

    # Creation of the list of integer number not in the list sums of abundant
    non_abundant_sums = [n for n in range(1, 28124) if n not in sums_of_abundants]

    # Return the sum of the final list
    return sum(non_abundant_sums)

# Expected answer: 4_179_871
print(non_abundant_sum())