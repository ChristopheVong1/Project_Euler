def largest_prime_factors(number):

    """
    Finds the largest prime factor of a given number using prime number tracking approach

    Args: number (int): The number to factorize (>1)

    Returns: int: The largest prime factor of the input number
    """

    # Initialization with the first prime number list
    prime_number_list=[2]

    # Initialization of the prime factor list
    prime_factor_list=[]

    # Continue until the number is reduced to 1
    while number!=1:

        # Check if the current largest known prime is a factor
        if number%prime_number_list[-1]==0:
            # Add the prime factor to our list
            prime_factor_list.append(prime_number_list[-1])
            # Reduce the number by the prime factor (using integer division)
            number=number//prime_number_list[-1]

        else:
            # If current prime doesn't divide, find the next prime number
            next_prime_number=prime_number_list[-1]+1

            # Infinite loop until next prime
            while True:
                # Assume candidate is prime until proven otherwise
                is_prime=True

                # Check divisibility against all known primes
                for p_number in prime_number_list:
                    if next_prime_number%p_number==0:
                        is_prime=False
                        break

                if is_prime==True:
                    # Add new prime to the list and exit search
                    prime_number_list.append(next_prime_number)
                    break
                else:
                    # Try next candidate
                    next_prime_number+=1

    # Returns the last element which is the largest prime factor
    return prime_factor_list[-1]

print(largest_prime_factors(600851475143))