def power_digit_sum(exponent):
    """
    The program computes the sum of a number which calculates 2 to a specific exponent
    Args: exponent (int): Exponent to compute the number
    Return: int: The sum of the digit of the calculated number using the exponent
    """

    # Computing the number with the exponent
    number=2**exponent
    # Conversion into a string for number manipulation
    converted_number=str(number)
    # Initialization of the digit list
    digit_list=[]
    
    # Iteration through the string to create the digit list
    for digit_index in range(0,len(converted_number),1):
        digit_list.append(int(converted_number[digit_index]))

    # Return the sum of the digit of the number created
    return sum(digit_list)

# Expectation 26
print(power_digit_sum(15))
# Expectation 1366
print(power_digit_sum(1000))