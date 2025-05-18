def nth_prime(number):

    """
    Finds the Nth prime number

    Args: number (int): The number of prime number to calculate

    Returns: int: The Nth prime number
    """

    # Initialization with the first prime number list
    prime_number_list=[2]

    while len(prime_number_list)<number:

        # Initialization of next prime number
        next_prime_number=prime_number_list[-1]+1

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
    return prime_number_list[-1]

print(nth_prime(6))
print(nth_prime(10001))