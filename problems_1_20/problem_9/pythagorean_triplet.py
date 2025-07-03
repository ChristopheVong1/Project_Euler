def pythagorean_triplet():
    """
    Iterate through possible values of 'a' (1 ≤ a < 333, since a < b < c
    and a + b + c = 1000)
    """

    for a in range(1,333,1):
        for b in range(a, int((1000-a)/2), 1):
            # Calculate c using the Pythagorean theorem
            c=(a**2+b**2)**(1/2)
            # Check is c is an integer (a²+b² is a perfect square)
            
            if c.is_integer():
                c=int(c)
            
                # Verify if the triplet sums to 1000
                if a+b+c==1000:
                    # Return the valid triplet and its product
                    return [a,b,c], a*b*c
            
# Execute and print the result
print(pythagorean_triplet())