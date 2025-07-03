from datetime import datetime

def counting_sundays():
    """
    Count every Sundays from 1 Jan 1901 to 31 Dec 2000
    Args: No Args
    Return: int: The number of sundays
    """

    # Initialization of the Sunday counter
    sunday_counter=0

    # Iteration through every year from 1901 to 2000
    for year in range(1901, 2001, 1):
        # Iteration through every month in a year
        for month in range(1,13,1):
           # Creation of the past date, we only check the first day of each month
            past_date=datetime(year,month,1)
            # Check if the past date is a Sunday
            if past_date.weekday()==6:
                # Increase the Sunday counter
                sunday_counter+=1                

    # Return the number of Sunday
    return sunday_counter

# Expected answer: 171
print(counting_sundays())