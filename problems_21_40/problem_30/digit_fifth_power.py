def digit_fifth_sum(n):
    """
    For a given number n, compute the sum of digit at fifth power
    Args: n(int): An integer
    Return: Return the sum of digit at fifth power for a number
    """
    # Conversion into string for digit access
    digits=str(n)
    # int() is used to turn back the value into int(), sum() to do the sum
    return sum([int(x)**5 for x in digits])

def digit_fifth_power():
    """
    Compute the sum of number that fulfill the condition: the sum of their digit at fifth power equals the original number (see Description for math)
    Args: None
    Return: The sum asked
    """

    # List of every number that fulfills the condition asked
    result=[]
    # Iteration through every number under the limit asked (see Description), 1 doesn't count
    for i in range(2,354295):
        # Check the condition
        if i==digit_fifth_sum(i):
            result.append(i)
    # The end result is the sum of the list that fulfills the condition
    return sum(result)

# Expected answer: 443 839
print(digit_fifth_power())