from math import sqrt

def is_pentagon(num):
    """
    Check if a number num is a pentagon (see description)
    Arg: num(int): An integer to test
    Return: A boolean
    """
    test1=sqrt(1+24*num)
    test2=abs(1+sqrt(1+24*num))
    return test1==int(test1) and test2%6==0

def generate_pentagon(n):
    """
    Compute the nth pentagon number
    Arg: n(int): An integer >=1
    Return: The nth pentagon number
    """
    return n*(3*n-1)/2

def pentagon_numbers():
    """
    Find a pair of pentagon numbers whose sum and differences are pentagon AND the difference is minimum (see description for strategy)
    Arg: None
    Return: The pair that fulfills the conditions
    """
    # Initialization
    flag=True
    k=2

    # Loop until we find the pair
    while flag:
        Pk=generate_pentagon(k)
        for j in range(1,k,1):
            Pj=generate_pentagon(j)
            if is_pentagon(Pk+Pj) and is_pentagon(Pk-Pj):
                solution_pair=(k,j)
                flag=False
        k+=1

    # Return the answer
    return solution_pair

# Expected answer: (2167,1020)
print (pentagon_numbers())