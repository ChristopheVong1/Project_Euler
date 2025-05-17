"""
Find the largest palindrome with are product of two 3-digit numbers
"""

def palindrome_check(number):
    
    """
    Checks if a number is a palindrome
    Args: number(int): The number to check for palindrome
    Returns: bool: True if the number is a palindrome, False otherwise
    """

    # Convert number to string for character access
    number_string=str(number)
    size_number=len(number_string)
    # Assume palindrome otherwise
    flag=True

    # Compare characters symmetrically from start and end
    for i in range(1, size_number//2+1, 1):
        # If characters don't match
        if number_string[i-1]!=number_string[-i]:
            flag=False
            # Exit if non palindrome
            break
    return flag

def factors_list():
    """
    Generates a list of all products of twi 3-digit numbers (100-999)
    Returns: list: Contains all possible products of 3 digit * 3 digit numbers (not sorted)
    """
    
    factors_list=[]
    for x in range (100,999,1):
        for y in range (100, 999, 1):
            factors_list.append(x*y)
    return factors_list

def palindrome_factor_list():
    """
    Finds the largest palindrome number that is a product of two 3-digit numbers
    Returns: int: The largest palindrome product found
    """

    # Get all possible products
    full_list=factors_list()

    # Initialization of the palindrome list
    palindrome_list=[]

    # Filter for palindrome numbers
    for number in full_list:
        if palindrome_check(number)==True:
            palindrome_list.append(number)

    # Return the largest palindrome found
    return max(palindrome_list)

print(palindrome_factor_list())