def number_to_words(n):

    """
    Convert number to word by combination and conditional depending on the range
    Args: n: int: Number to convert
    Return: The number as word
    """

    # Number out of bound for the problem
    if n < 1 or n > 1000:
        return ""
    
    # List of words for numbers
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]

    # Edge case for 1000
    if n == 1000:
            return "onethousand"
        
    # Initialization of the result
    res = ""
    # Compute how many hundred
    hundred = n // 100
    # Remainder for number above one hundred
    remainder = n % 100
        
    # Creation of the word associated above 100
    if hundred > 0:
        res += units[hundred] + "hundred"
        if remainder > 0:
            res += "and"

    # Creation of the word from 1 to 20
    if remainder < 20:
        res += units[remainder]
    else:
        # Creation of the word from 21 to 99
        res += tens[remainder // 10] + units[remainder % 10]
    
    # Return the result
    return res

def number_letter_count():
    """
    Calculate the sum of the letters for every number from 1 to 1000
    No Args
    Return: int: The sum of the letter count
    """
    
    # Initialization of the sum
    sum_letters=0

    # Iteration through every number from 1 to 1000
    for i in range(1,1001):
        word=number_to_words(i)
        sum_letters+=len(word)
    
    # Return the sum
    return sum_letters 

# Expectation 21124
print(number_letter_count())