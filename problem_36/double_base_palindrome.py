def ispalindrome(n):
    """
    Check if a number n is a palindrome
    Arg: n(int): An integer to test
    Return: Boolean depending on the result
    """
    # Conversion into string for digit access and compare it to the reverse version
    return str(n)==str(n)[::-1]

def base10to2(n):
    """
    Convert a base 10 number to base 2, we can use the function bin()
    Arg: n(int): A base 10 integer
    Return: int: A base 2 integer
    """
    # bin() convert to base 2, [2:] remove the prefix "0b"
    return bin(n)[2:]

def double_base_palindrome(max):
    """
    Find every double base palindrome under the number max
    Arg: max(int): The maximum number to test
    Return: int: The sum of every double base palindrome under max
    """

    # Initialization
    double_base_pal_list=[]

    # Iteration through every number until max
    for i in range(max+1):
        if ispalindrome(i) and ispalindrome(base10to2(i)):
            double_base_pal_list.append(i)
    
    # Return the sum of every number that fulfills the condition
    return sum(double_base_pal_list)

# Expected answer: 872_187
print(double_base_palindrome(1000000))