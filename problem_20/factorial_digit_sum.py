import math

def factorial_digit_sum(n):
    """
    Calculate the sum of the digit of factorial n
    Arg: int: The number to compute n!
    Return: The result of factorial n
    """

    # Compute the factorial n
    factorial=math.factorial(n)

    # Conversion into a string for number manipulation
    converted_number=str(factorial)

    # Initialization of the digit list
    digit_list=[]
    
    # Iteration through the string to create the digit list
    for digit_index in range(0,len(converted_number),1):
        digit_list.append(int(converted_number[digit_index]))

    # Return the result
    return sum(digit_list)

# Expected answer: 27
print(factorial_digit_sum(10))
# Expected answer:
print(factorial_digit_sum(100))