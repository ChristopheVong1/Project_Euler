from fibonacci_maker import fibonacci_maker
from even_sum import even_sum

def problem_2(max_number):

    """
    Solves Project Euler problem 2

    This function:
    1. Generates a Fibonacci sequence up to but not exceeding max_number
    2. Filters and sums the even-valued terms in this sequence
    
    Args: max_number (int): The upper limit for Fibonacci number generation. Must be a positive integer.
        
    Returns: int: The sum of all even-valued Fibonacci numbers below max_number.
    """
    
    fibonacci_list=fibonacci_maker(max_number)

    return even_sum(fibonacci_list)

print(problem_2(40_000_000))