from math import sqrt

def generate_hexagon(n):
    """
    Compute the nth hexagon number
    Arg: n(int): An integer >=1
    Return: The nth hexagon number
    """
    return n*(2*n-1)

def is_pentagon(num):
    """
    Check if a number num is a pentagon (see description)
    Arg: num(int): An integer to test
    Return: A boolean
    """
    test1=sqrt(1+24*num)
    test2=abs(1+sqrt(1+24*num))
    return test1==int(test1) and test2%6==0

def triangular_pentagonal_hexagonal():
    """
    Find the first number after 40755 that is triangular, pentagonal and hexagonal
    Arg: None
    Return: Return the correct integer
    """

    # Initialization
    n=144

    # Iteration until the answer meets the condition
    while not is_pentagon(generate_hexagon(n)):
        n+=1

    # Return the correct integer
    return generate_hexagon(n)

# Expected answer: 1_533_776_805
print(triangular_pentagonal_hexagonal())