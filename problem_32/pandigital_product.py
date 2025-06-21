def is_pandigital(s):
    """
    Check if a string (of a number) is pandigital 1-9 (contain every digit from 1 to 9 once)
    Arg: s(int): A string (that represent a number) to test
    Return: bool: A boolean depending if pandigital or not
    """
    # The length must be exactly 9 and every char from 1-9 must be included
    return len(s) == 9 and set(s) == set('123456789')

def pandigital_products():
    """
    Find the sum of all products whose multiplicand / multiplier / product identity is 1-9 pandigital
    Arg: None
    Return: The answer for Euler problem 32
    """
    # Initialization of every product that fulfill the condition (set() is used to keep the value once)
    products = set()

    # Check 1-digit x 4-digit
    for a in range(1, 10):
        for b in range(1000, 10000):
            c = a * b
            # Concatenation of a, b and c
            s = f"{a}{b}{c}"
            # If pandigital, we add the result of the products set
            if is_pandigital(s):
                products.add(c)
    
    # Check 2-digit x 3-digit
    for a in range(10, 100):
        for b in range(100, 1000):
            c = a * b
            s = f"{a}{b}{c}"
            if is_pandigital(s):
                products.add(c)
    
    # Return the answer
    return sum(products)

# Expected answer: 
print(pandigital_products())