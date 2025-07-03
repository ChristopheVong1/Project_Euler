def is_pandigital(s):
    """
    Check if a string (of a number) is pandigital 1-9 (contain every digit from 1 to 9 once)
    Arg: s(int): A string (that represent a number) to test
    Return: bool: A boolean depending if pandigital or not
    """
    # The length must be exactly 9 and every char from 1-9 must be included
    return len(s) == 9 and set(s) == set('123456789')

def pandigital_multiples():
    """
    Find the highest number that can be concatenated as a product and that is a 9 digit pandigital
    Args: None
    Return: The highest value that fulfills the condition
    """

    # Initialization
    largest_pandigital=0

    # Iteration in reverse order because we want the biggest
    for base in range(1,9877):
        
        # Initialization
        concatenated_product=""
        n=1

        # Creation of the concatenated product using the base
        while len(concatenated_product)<9:
            concatenated_product+=str(base*n)
            n+=1

        # Check if the concatenated product is a valid 9-digit pandigital
        if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
            current_pandigital = int(concatenated_product)
            if current_pandigital > largest_pandigital:
                largest_pandigital = current_pandigital

    # Return the biggest value that fulfills the condition
    return largest_pandigital

# Expected answer: 932_718_654
print(pandigital_multiples())