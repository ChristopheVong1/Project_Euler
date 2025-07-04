def count_pythagorean_triples(p):
    """
    Counts the number of integer right-angled triangles with perimeter 
    p.
    Args: p (int): Perimeter of the triangle.
    Returns: int: Number of valid Pythagorean triples for the given 
    perimeter.
    """

    # Initialization of number of valid triplet
    count = 0
    # Iterate possible values for side a (the smallest side)
    for a in range(1, p // 3):
        # Given a and p, derive b from the perimeter constraint 
        # and check if it's valid (easy math using the 2 equations)
        numerator = p * (p - 2 * a)
        denominator = 2 * (p - a)
        if numerator % denominator != 0:
            continue  # b must be integer
        b = numerator // denominator
        if b <= a:
            continue  # Ensure a <= b < c
        c = p - a - b
        # Check Pythagorean theorem
        if a * a + b * b == c * c:
            count += 1
    # Return the number of triplet
    return count

def integer_right_triangles(p_max):
    """
    Find the highest value p under p_max that create the most amount of
    triplet such as a+b+c=p and a2+b2=c2, a, b and c are integers.
    Arg: p_max(int): An integer
    Return: The value p that fulfills the condition
    """
    
    # Initialization
    best_p = 0
    max_count = 0
    # Check all possible perimeters
    for p in range(1, p_max + 1):
        current_count = count_pythagorean_triples(p)
        if current_count > max_count:
            max_count = current_count
            best_p = p
    return best_p

# Expected answer: 840
print(integer_right_triangles(1000))