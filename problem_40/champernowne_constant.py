def champernowne_constant():
    """
    Compute the product of specific digits in the irrational decimal 
    fraction (see description of problem 40)
    Arg: None
    Return: The product of the digits at 1, 10, ..., 1000000 positions
    """

    # Initialization
    irrational_fraction=""
    count=1

    # Iteration
    while len(irrational_fraction)<1000000:
        irrational_fraction+=str(count)
        count+=1

    print(int(irrational_fraction[0]))
    print(int(irrational_fraction[9]))
    print(int(irrational_fraction[99]))
    print(int(irrational_fraction[999]))
    print(int(irrational_fraction[9999]))
    print(int(irrational_fraction[99999]))
    print(int(irrational_fraction[999999]))
    print(len(irrational_fraction))  
    # Return the product of specific digits in the irrational decimal fraction
    return int(irrational_fraction[0])*int(irrational_fraction[9])*int(irrational_fraction[99])*int(irrational_fraction[999])*int(irrational_fraction[9999])*int(irrational_fraction[99999])*int(irrational_fraction[999999])

# Expected answer: 210 (but maybe need to double check the answer)
print(champernowne_constant())