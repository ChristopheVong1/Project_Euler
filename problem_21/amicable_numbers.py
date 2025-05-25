def proper_divisor(n):
    """
    Calculate the proper divisors of n by testing every value from 1 to n (excluded) and return the sum of the divisors
    Args: n(int): The number to test 
    Return: The sum of the proper divisors
    """

    # Edge case for n=1
    if n == 1:
        return 0

    # Initialization of the divisor list
    divisor_list=[1]

    # Iteration through every number from 1 to sqrt(n)
    for i in range(2,int(n**0.5),1):
        # Check divisibility
        if n%i==0:
           divisor_list.append(i)
           if i != n // i:  
                divisor_list.append(n // i)
    
    return sum(divisor_list)

def check_amicable(a,b):
    """
    Check if 2 numbers a and b are amicable pairs
    Args: int: a and b are the integer to compare
    Return: True or False if amicable or not
    """
    return proper_divisor(a)==b and proper_divisor(b)==a and a!=b

def amicable_number_sum(n):
    """
    We calculate the sum of all amicable numbers under n
    Args: n(int): Upper ceiling of amicable numbers
    Return: The sum of all amicable numbers under n
    """

    # Initialization of the amicable number set (to avoid duplicate)
    amicable_number_list=set()

    # Iteration through every number from 1 to n
    for a in range(1,n+1,1):
        b=proper_divisor(a)
        if b>a and b<n:
            if check_amicable(a,b):
                amicable_number_list.add(a)
                amicable_number_list.add(b)

    # Return the sum of all amicable numbers
    return sum(amicable_number_list)

# Expected answer: 31626
print(amicable_number_sum(10000))    