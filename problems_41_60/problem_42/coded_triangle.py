import os

def word_value(string):
    """
    Compute a word value using the letter of string (A=1, ..., Z=26)
    Arg: string: Words in upper case
    Return: int: The word value
    """
    # Initialization
    word_value=0

    # Iteration through every character
    for char in string:
        # ord() is used to compute a value based on the position of the char in the alphabet
        word_value+=ord(char)-ord("A")+1

    # Return
    return word_value

def create_triangle_numbers(limit):
    """
    Create a list of triangle numbers up to the limit using the formula
    Arg: limit(int): A number to not exceed for the triangle numbers list
    Return: A list of triangle numbers
    """
    # Initialization
    triangle_numbers=[1]
    i=2

    # Creation of triangle numbers until the last value exceed the limit
    while triangle_numbers[-1]<limit:
        triangle_numbers.append(i*(i+1)//2)
        i+=1

    # Return the list
    return triangle_numbers

def extract_words(filename):
    """
    Read the file .txt and convert it into a list of words
    Arg: file: A .txt file in the same folder
    Return: A list of string for each words in the original file
    """

    project_folder = r'D:\Programmation\Python\Project_Euler\problems_41_60\problem_42'  # Replace with actual path
    os.chdir(project_folder)

    # Read the words from the file
    with open(filename, 'r') as file:
        words = file.read().replace('"', '').split(',')

    # Return the list
    return words

def coded_triangle(filename):
    """
    Find the number of triangle words in a given file
    Arg: file: A .txt file containing words
    Return: The number of triangle words in the file
    """
    # Initialization of counter for triangle words
    count=0

    # Creation of triangle number, we choose a limit of 2000
    limit=2000
    triangle_numbers=create_triangle_numbers(limit)

    # Extracting the list of words
    words=extract_words(filename)

    # Iteration through every word list
    for word in words:
        if word_value(word) in triangle_numbers:
            count+=1

    # Return the counter for triangle words
    return count

# Expected answer: 162
print(coded_triangle("0042_words.txt"))