#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Arnie Lloyd Sarmiento"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
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
    "Print a usage message to the user"
    ...

def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
