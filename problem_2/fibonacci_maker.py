def fibonacci_maker(max_number):
    
    """
    Generates a Fibonacci sequence up to, without exceeding, a specified maximum number

    Args: max_number (int): Upper limit for the Fibonacci sequence

    Returns: list: A list containing the Fibonacci sequence up to the largest number less than max number
    """

    # Initialize the sequence with the first two Fibonacci numbers
    fibonacci_list=[0, 1]

    # Generate sequence while the last number is less than max_number
    while fibonacci_list[-1]<max_number:
        # Calculate the next Fibonacci number
        next_value=fibonacci_list[-2]+fibonacci_list[-1]

        # Exit condition: stop if we reach or exceed max_number
        if next_value>=max_number:
            break

        # Append the valid number to the sequence
        fibonacci_list.append(next_value)

    return fibonacci_list

print(fibonacci_maker(100))