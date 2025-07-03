from math import factorial

def is_curious(n):
    """
    Check if a number is curious (it equals to the sum of the factorials of their digits)
    Arg: n(int): The integer to test
    Return: bool: Boolean depending of if it fulfills the condition or not
    """
    # Initialization of sum of factorials of digits
    sum_factorial=0
    # str() for digit access
    for digit in str(n):
        sum_factorial+=factorial(int(digit))
    # Check the equality between the number and the sum
    return n==sum_factorial

def digit_factorials():
    """
    Find the sum of every curious number by brute forcing (see Description for bounds)
    Arg: None
    Result: The sum of every curious number
    """
    # Initialization of curious number list
    curious_list=[]
    # See description to explain the bounds
    for i in range (10,2540160):
        # If the number is curious, we add it to the list
        if is_curious(i):
            curious_list.append(i)
    # Return the sum of the list
    return sum(curious_list)

# Expected answer: 40730
print(digit_factorials())