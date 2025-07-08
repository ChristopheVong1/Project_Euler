from itertools import permutations

def is_pandigital(s, n=None):
    """
    Check if a string (of a number) is pandigital (contain every digit 
    from 1 to n once)
    Arg: s(int): A string (that represent a number) to test
    n(int): The expected length
    Return: bool: A boolean depending if pandigital or not
    """

    return len(s) == 10 and set(s) == set(str(d) for d in range(0, 10))
   
def is_substring_divisible(num):
    """
    Check if a 10 digit number fulfills the sub string divisibility condition of Euler problem 43
    Args: num(int): A 10 digit number (ideally pandigital)
    Return: A boolean if the condition is fulfilled or not
    """
    # str() to get access to the digits
    digits=str(num)
    if len(digits)!=10:
        return False

    # Create a new number based on the digits and then check the divisibility
    num234=int(digits[1:4])
    if num234%2!=0:
        return False
    
    num345=int(digits[2:5])
    if num345%3!=0:
        return False
    
    num456=int(digits[3:6])
    if num456%5!=0:
        return False
    
    num567=int(digits[4:7])
    if num567%7!=0:
        return False
    
    num678=int(digits[5:8])
    if num678%11!=0:
        return False
    
    num789=int(digits[6:9])
    if num789%13!=0:
        return False
    
    num8910=int(digits[7:10])
    if num8910%17!=0:
        return False

    # Return True if every test are correct
    return True

def sub_string_divisibility():
    """
    Find every 10 digits pandigital that fulfill a specific sub string divisibility condition, then return the sum of the list
    Arg: None
    Return: The sum of every 10 pandigital numbers with the wanted property
    """

    # Initialization
    final_list=[]

    # Iteration through every 10 digit number using permutations
    for p in permutations('0123456789',10):
        p_str=''.join(p)
        if is_pandigital(p_str):
            p_int=int(p_str)
            if is_substring_divisible(p_int):
                final_list.append(p_int)

    # Return the sum of the final list
    return sum(final_list)

# Expected answer: 16_695_334_890
print(sub_string_divisibility())