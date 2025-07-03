def extract_file(file_name):
    """
    Open the file and extract the names as a list and also sorted
    Args: file_name: the name of the .txt file
    Return: A list with every name sorted alphabetically
    """

    # Open the file in reading mode
    with open(file_name, "r") as file:
        # file.read() to get the full list as a single string
        # Then replace() to remove the double quotes (else we got two double quotes in the final list)
        # Then split() to transform the string into a list using commas as separators
        names=file.read().replace('"','').split(',')

    # Sort the names alphabetically
    names.sort()

    # Return the name list sorted
    return names

def letter_value(char):
    """
    Convert the char into a score depending on its position in the alphabetical order
    Args: char: Character to convert
    Return: The value of char
    """

    # Alphabetical list
    alphabet="abcdefghijklmnopqrstuvwxyz"

    # Return the index (+1 because start at 0) using index()
    return alphabet.index(char.lower())+1

def name_value(name):
    """
    Convert the name into a score depending on the letter that constitute the name
    Args: string: Name to convert
    Return: The value of name
    """

    # Initialization of the name value
    name_value=0

    # Iteration through every char in name
    for char in name:
        name_value+=letter_value(char)
    
    # Return the final value
    return name_value

def name_scores(file_name):
    """
    Extract the name in the files, then give a score for each name depending on its letter value and its position
    Args: file_name: Name of the file
    Return: The sum of the score of every name
    """

    # Initialization of final score
    final_name_scores=[]

    # Extraction of every name in the file
    names_list=extract_file(file_name)

    # Iteration through every name in the file
    for i in range(len(names_list)):
        # Calculation of the name score depending on its position and letter values
        final_name_scores.append(name_value(names_list[i])*(i+1))
    
    # Return final result
    return sum(final_name_scores)

# Expected result: 871198282
print(name_scores(r"D:\Programmation\Python\Project_Euler\problem_22\0022_names.txt"))