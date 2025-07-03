def sum_prime(number):

    """
    Finds every prime number under a specific number

    Args: number (int): The upper bound of the prime number list

    Returns: int: The sum of the prime number list
    """

    # Edge case for number <=2
    if number <= 2:
        return 0

    # Initialization with the first prime number list
    prime_number_list=[2]

    while prime_number_list[-1]<number:

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

    # Returns the sum of all prime below number
    return sum(prime_number_list)-prime_number_list[-1]

print(sum_prime(10))
# Print 142913828922, need a few minutes
print(sum_prime(2000000))