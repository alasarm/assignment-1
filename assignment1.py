#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: CSN
Author: "Arnie Lloyd Sarmiento"
The python code in this file (assignment1.py) is original work written by
"Arnie Lloyd Sarmiento". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys


def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for February in a leap year
    if month == 2 and leap_year(year):
        return 29

    # Return the maximum days in the specified month
    return days_in_month[month - 1]


def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''

    str_year, str_month, str_day = date.split('-') # Split the input date string into its components: year, month, and day
    year = int(str_year) # Convert the string components into integers for calculations, takes the year
    month = int(str_month) # Convert the string components into integers for calculations, takes the month
    day = int(str_day) # Convert the string components into integers for calculations, takes the day

    # Calculate the next day by adding 1 to the current day
    tmp_day = day + 1  # next day

    # Check if the next day exceeds the maximum number of days in the current month
    if tmp_day > mon_max(month, year): # If it does, wrap around to the first day of the next month
        to_day = 1  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1 # Move to the next month
    else:
    # If it doesn't exceed, keep the same month and use the calculated day
        to_day = tmp_day
        tmp_month = month + 0 # Stay in the current month

    # Check if the next month exceeds December (month 12)
    if tmp_month > 12:
        to_month = 1 # Wrap around to January (month 1)
        year += + 1 # Increment the year
    else:
        to_month = tmp_month # If it doesn't exceed, use the calculated month, Stay in the current year
    next_date = f"{year}-{to_month:02}-{to_day:02}" # Format the next date into a string in YYYY-MM-DD format
    return next_date # Return the calculated next day's date as a string


def usage():
    "print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    # Ensure the date is in the correct format: YYYY-MM-DD
    
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        return False
    try:
        # This will split the date into year, month, and day
        year, month, day = map(int, date.split('-'))

        # This is to check if the month is a valid month (1-12)
        if month < 1 or month > 12:
            return False

        # This is to check if the day is valid for the month/year
        if day < 1 or day > mon_max(month, year):
            return False
        return True

    # This line will be used to handle errors where the date is not in the correct format/cannot be converted. 
    except ValueError:
        return False


def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    count = 0
    current_date = start_date

    # This will loop through days starting from the start_date to stop_date
    while True:
        year, month, day = map(int, current_date.split('-'))# Check if the current day is a weekend (Saturday or Sunday)
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1

        # This will stop the loop whem the current date is equal to the stop date
        if current_date == stop_date:
            break

        # Next day
        current_date = after(current_date)

    return count


if __name__ == "__main__":
    # This is to check if the correct number of arguments are passed
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    # This checks if the dates are valid
    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # This line ensures start_date is earlier than end_date
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    # This will calculate the number of weekend days
    weekend_days = day_count(start_date, end_date)
    

    print(f"The period between {start_date} and {end_date} includes {weekend_days} weekend days.")
