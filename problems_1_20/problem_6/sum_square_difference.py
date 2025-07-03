def sum_square(number):
    """
    Calculates the sum of squares of the first 'number' natural numbers.
    
    Args:
        number (int): Upper limit of natural numbers to consider 
        (inclusive)
        
    Returns:
        int: Sum of squares from 1² to number²
        
    Formula:
        sum = 1² + 2² + ... + number²
    """
    
    result=0
    for i in range(number):
        # Add square of each number (1-based index)
        result+=(i+1)**2
    return result

def square_sum(number):
    """
    Calculates the square of the sum of the first 'number' natural numbers.
    
    Args:
        number (int): Upper limit of natural numbers to consider 
        (inclusive)
        
    Returns:
        int: Square of the sum from 1 to number
        
    Formula:
        sum = (1 + 2 + ... + number)²
    """

    sum=0
    for i in range(number):
        # Accumulate sum of numbers (1-based index)
        sum+=i+1
    # Return squared sum
    return sum**2

def sum_square_difference(number):
    """
    Calculates the difference between the square of the sum and the sum 
    of squares
    for the first 'number' natural numbers
    
    Args:
        number (int): Upper limit of natural numbers to consider
        
    Returns:
        int: (square_of_sum) - (sum_of_squares)
    """

    square_sum_value=square_sum(number)
    sum_square_value=sum_square(number)
    return square_sum_value-sum_square_value

print(sum_square(100))
print(square_sum(100))
print(sum_square_difference(100))