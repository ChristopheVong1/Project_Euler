def collatz_seq(n):
    """
    Calculate the Collatz sequence but we only look at the length to save memory
    Arg: n (int): Starting number of the Collatz sequence
    Return: The length of the Collatz list
    """

    # Initialization of length
    length=1

    # Iteration until we reach n=1
    while n!=1:
        # Check if last number is even or odd and calculate the next sequence
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        length+=1

    # Return the length collatz_list
    return length

def longest_collatz_seq(max_number):
    """
    Find the longest chain of Collatz sequence under max_number
    Arg: max_number (int): How many number to test from 1 to max_number
    Return: The starting number of the longest Collatz sequence
    """

    # Initialization of the starting number
    index=0
    longest_chain=0

    # Iteration through every number until max_number
    for number in range(1, max_number+1):

        # Check if the new sequence is longer than previous max
        if collatz_seq(number)>longest_chain:
            index=number
            longest_chain=collatz_seq(number)

    # Return starting number that provides the longest chain
    return index

# Expected answer is 837799
print(longest_collatz_seq(1_000_000))