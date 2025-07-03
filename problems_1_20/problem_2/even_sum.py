def even_sum(numbers):

    """
    Calculates the sum of all even numbers in a given list.

    Args: numbers(list): A list of integers to process.

    Returns: int: The sum of all even numbers in the input list. 0 if there are no even numbers of if the list is empty.
    """

    # Initialize an empty list to store even numbers
    even_list=[]

    # Iterate through each number in the input list
    for number in numbers:

        # Check if the number is even (divisible by 2 with no remainder)
        if number%2==0:
            # Add even number to our list
            even_list.append(number)

    # Return the sum of all collected even numbers
    return sum(even_list)