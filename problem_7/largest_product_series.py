def slice_extractor(size_slice, index, list):
    """
    Extracts a continuous sublist of digits from the main list.
    
    Args:
        size_slice: Length of the sublist to extract
        index: Starting position for extraction
        digit_list: The list of digits to extract from
        
    Returns:
        A sublist of length size_slice starting at index
        
    Raises:
        IndexError: If index is out of valid range
    """

    if index<0 or index>len(list)-size_slice:
        raise IndexError("L'indice index est hors limite.")
    return list[index:index+size_slice]

def product_list(list):
    """
    Calculates the product of all digits in the input list.
    
    Args:
        digits: List of single-digit integers
        
    Returns:
        The product of all digits
    """

    result=list[0]
    for i in range (1,len(list),1):
        result*=list[i]
    return result

def largest_product_series(size_slice, list):
    """
    Finds the continuous sublist of given length with the largest digit product.
    
    Args:
        size_slice: Length of sublists to consider
        digit_list: The list of digits to analyze
        
    Returns:
        A tuple containing:
        - The maximum product found
        - The sublist that produces this product
    """

    list_product=[]

    # Iterate through all possible starting positions
    for i in range (len(list)-size_slice+1):
        # Extract current window of digits
        tested_slice=slice_extractor(size_slice, i, list)
        # Calculate and store product
        list_product.append(product_list(tested_slice))

    greatest_product=max(list_product)
    max_index=list_product.index(greatest_product)
    return greatest_product, slice_extractor(size_slice,max_index,list)

# The large 1000-digit number as a multi-line string
target_number="""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""

# Convert the multi-line string into a list of single-digit integers
# Remove newline characters first to avoid conversion errors
cleaned_target_number=[int(char) for char in target_number.replace("\n","")]

# Problem solutions (Project Euler Problem 8)
print(largest_product_series(4, cleaned_target_number))
print(largest_product_series(13, cleaned_target_number))