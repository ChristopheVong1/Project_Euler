from math import gcd

def digit_cancelling():
    """
    Find the four non trivial fraction that fulfill digit cancelling as explained in Euler project 33
    Args: None
    Return: The product of the four fractions given in its lowest common terms, and find the value of the denominator
    """
    
    # Initialization of the final product of the four fractions
    numerator_product = 1
    denominator_product = 1
    
    # Iteration through every 2-digit number for numerator
    for numerator in range(10,100):
        # Same but numerator+1 ensure that denominator>numerator
        for denominator in range(numerator+1,100):
            # Compute the value of the four digit as ab/cd
            a = numerator // 10
            b = numerator % 10
            c = denominator // 10
            d = denominator % 10
            # Case where 2nd digit of numerator cancel the 1st digit of denominator
            if b == c and b != 0:
                if (numerator * d) == (denominator * a):
                    numerator_product *= a
                    denominator_product *= d
            # Case where 1st digit of numerator cancel the 2nd digit of denominator
            if a == d and a != 0:
                if (numerator * c) == (denominator * b):
                    numerator_product *= b
                    denominator_product *= c

    # Simplify the product
    common_divisor=gcd(numerator_product,denominator_product)
    return denominator_product//common_divisor

# Expected answer: 100
print(digit_cancelling())