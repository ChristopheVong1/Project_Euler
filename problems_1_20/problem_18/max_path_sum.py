def convert_triangle(triangle):
    """
    Convert a triangle as string format into a list (pyramid form)
    Args: The triangle as string format
    Return: The triangle as a list format
    """

    # Initialization of the list of lines
    lines=[]
    # Iteration through the triangle list after they get split after \n
    for line in triangle.split("\n"):
        # We remove the space between each number in each line
        stripped_line = line.strip()
        # Add non-empty lines
        if stripped_line:
            lines.append(stripped_line)

    # Initialization of the triangle as list
    new_triangle=[]

    # Conversion of the line list (string) into a list of integer as lines
    for line in lines:
        row=[int(number) for number in line.split()]
        new_triangle.append(row)

    # Return the triangle string into the triangle integer
    return new_triangle

def max_path_sum(triangle):
    """
    First convert the triangle "string" into a list. Then, add from 
    the second to last row with the last row and move upwards by only
    keeping the max result
    Args: triangle (str): String that contain the numbers as a pyramid
    Return: int: Maximum path sum in the triangle
    """

    # Conversion triangle
    converted_triangle=convert_triangle(triangle)

    # Iteration from the second last row to the first by going in the
    # reverse order
    for row in range(len(converted_triangle)-2, -1, -1):
        # Iteration through every column of the current row
        for col in range(len(converted_triangle[row])):
            # Update current cell by adding with max of the two adjacent cells below
            converted_triangle[row][col]+=max(converted_triangle[row+1][col], converted_triangle[row+1][col+1])

    # Return the maximum sum path    
    return converted_triangle[0][0]

triangle="""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# Expected answer = 1074
print(max_path_sum(triangle))