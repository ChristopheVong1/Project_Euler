def digit_count(n):
    """
    Count the number of digit inside a number n
    Args: n(int): An integer to analyse
    Return: int: The number of digit
    """
    return len(str(n))

def digit_fibonacci_number(digit_threshold):
    """
    Compute the fibonacci until the first term has a number of digits 
    that exceed the digit_threshold
    Args: digit_threshold(int): The number of digit to exceed
    Return: Return the index of the first term that fulfill the condition
    """

    # Initialization (don't make a list to avoid storing)
    first_term=1
    second_term=1
    count=2

    # Iteration until condition fulfilled
    while digit_count(second_term)<digit_threshold:
        count+=1
        next_term=first_term+second_term
        first_term=second_term
        second_term=next_term

    # Return the final result
    return count

# Expected answer: 12
print(digit_fibonacci_number(3))
# Expected answer: 4782
print(digit_fibonacci_number(1000))