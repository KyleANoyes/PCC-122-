#******************************************************************************
# Author:           Kyle Noyes
# Lab:              Lab 3
# Date:             2/13/2022
#
# Description:      This program calculates what the end of year bonus amount
#                   and contributions to employee'sprofit sharing accounts will 
#                   be and if they are eligable for a bonus or not. 
#
# Input:            Program first seeks the type of employment, pay, number of
#                   hours worked since Jan 1st, and base company contributions.

# Output:           (Summary of messages displayed by the program)
# Sources:          Lab 3 specifications and video. Also a downright unhealthy 
#                   amount of research/staring at stack overflow           
#******************************************************************************

# No global variables are used
# Begin eoy_bonus main function

def eoy_bonus():

    # Identify the status of the employee type
    # Use the calculator relevant to employee type
    status = get_status()
    if status == 1:
        contractor()
    elif status == 2:
        part_time()
    else:
        full_time()

# Contractor employee function
# Call get_rate function, set rate equal to function output
# Call get_hours worked function, set ytd_hours to function output
# Call get_contribute function, set contributions to function output
# 
# Contractors will never get a bonus, but will recieve a profit share match
# Call match_t function to calculate match, set match_t to function output
# Call contract function with match_t variable 

def contractor():
    rate = get_rate()
    ytd_hour = get_hours()
    contribute = get_contribute()
    match_t = get_match_true(rate, contribute, ytd_hour)
    contract(match_t)

# Part-time employee function
# Call get_rate function, set rate equal to function output
# Call get_hours worked function, set ytd_hours to function output
# Call get_contribute function, set contributions to function output

def part_time():
    rate = get_rate()
    ytd_hour = get_hours()
    contribute = get_contribute()
        
    # Check if ytd_hours is > 500
    # If true, employee is eligable for bonus. Use part_true to include bonus + match
    # Call get_bonus_true function with rate and ytd_hour var, set bonus_t = to output
    # Call get_match_true function with rate, contribute and ytd_hour var, set match_t = to output
    # Call part_true function with bonus_t and match_t variables
    #
    # If false, employee is not eligable for a bonus. Use part_false to include match
    # Call get_match_false with rate, contribute and ytd_hour var, set match_f = to output
    # Call part_false function with match_f variable
    if ytd_hour >= 500:
        bonus_t = get_bonus_true(rate, ytd_hour)
        match_t = get_match_true(rate, contribute, ytd_hour)
        part_true(bonus_t, match_t)
    else:
        match_f = get_match_false(rate, contribute, ytd_hour)
        part_false(match_f)

# Full-time employee function
# Call get_rate function, set rate equal to function output
# Call get_hours worked function, set ytd_hours to function output
# Call get_contribute function, set contributions to function output
# Call get_shares function, set shares to function output
# Call get_share_value function, set share_value to function output

def full_time():
    rate = get_rate()
    ytd_hour = get_hours()
    contribute = get_contribute()
    shares = get_shares()
    share_value = get_share_value()
    
    # Check if ytd_hours is > 1000
    # If true, employee is eligable for bonus. Use part_true to include bonus + match
    # Call get_bonus_true function with rate and ytd_hour var, set bonus_t = to output
    # Call get_match_true function with rate, contribute and ytd_hour var, set match_t = to output
    # Call full_true function with bonus_t, match_t, shares, and share_value variables
    #
    # If true, employee is not eligable for bonus. Use full_false to include match
    # Call get_match_false with rate, contribute and ytd_hour var, set match_f = to output
    # Call full_false function with match_f, shares, and share_value variables
    
    if ytd_hour >= 1000:    
        bonus_t = get_bonus_true(rate, ytd_hour)
        match_t = get_match_true(rate, contribute, ytd_hour)
        full_true(bonus_t, match_t, shares, share_value)
    else:
        match_f = get_match_false(rate, contribute, ytd_hour)
        full_false(match_f, shares, share_value)

# Function get_status
# This function is critical - This set the decision branch direction
# Expect only 3 possible values -- 1, 2, 3
# 1 = contractor, 2 = part time, 3 = full time
#
# Set status = 0
# Prompt user to input employmee's employment condition 1, 2, or 3
# If 1, return status as 1
# If 2, return status as 2
# Else, return status as 3

def get_status():
    status = 0
    status = int(input("\nPlease enter the employee's type of employment. \
Contractor = 1, Regular part-time = 2, Regular full-time = 3:"))
    if status == 1:
        status = 1
        return status
    elif status == 2:
        status = 2
        return status
    else:
        status == 3
        status = 3
        return status

# Function get_rate - employee hourly pay
# set rate = 0
# Ask user to input the hourly rate
# return rate = user inputed rate

def get_rate():
    rate = 0.00
    rate = float(input("\nPlease enter the employee's hourly pay rate: "))
    return rate

# Function get_hours
# Set hours = 0
# Ask user to input number of hours worked this year
# Truncate value down to single digit
# return hours = truncated user input

def get_hours():
    hours = 0
    hours = float(input("\nPlease input how many hours this employee has worked \
from since January 1's of this year: "))
    hours = (hours // 1)
    return hours

# Function get_contribute
# Set contribute = 0
# Ask user to input the company profit sharing match %
# Return hours = user inputed float/int

def get_contribute():
    contribute = 0
    contribute = float(input("\nPlease enter the profit share percnatage \
contribution from employee's wage (5% = 0.05): "))
    return contribute

# Function get_shares
# Set shares = 0
# Ask user to input the number of shares held by employee
# Return shares = user inputed float/int

def get_shares():
    shares = 0
    shares = float(input("\nPlease state number of shares owned by employee: "))
    return shares

# Function get_share_value
# Set value = 0
# Ask user to input the value of a single share
# Return value = user inputed float/int

def get_share_value():
    value = 0
    value = float(input("\nPlease input the value of a single share: "))
    return value

# Function get_bonus_true
# Grab rate and ytd_hour variable
# set bonus = 0
# set bonus = ((rate * 6%) * ytd_hour))
# return bonus value with arithmetic output

def get_bonus_true(rate, ytd_hour):
    bonus = 0.00
    bonus = ((rate * 0.06)) * ytd_hour
    return bonus

# Function get_match_true
# Grab rate, contribute, and ytd_hour variable
# set match = 0
# set match = 2,000 + (rate * contribute * ytd_hour)
# return match value with arithmetic output

def get_match_true(rate, contribute, ytd_hour):
    match = 0.00
    match = 2000.00 + ((rate * contribute) * ytd_hour)
    return match

# Function get_match_false
# Grab rate, contribute, and ytd_hour variable
# set match = 0
# set match = 1,000 + (rate * contribute * ytd_hour)
# return match value with arithmetic output

def get_match_false(rate, contribute, ytd_hour):
    match = 0.00
    match = 1000.00 + ((rate * contribute) * ytd_hour)
    return match


#******************************************************************************
# All final solutions passed into easy to read print statements

# Function welcome
# Displayt a welcome message to the user
def welcome():
    print("\nWelcome to the End-of-Year (EOY) employee bonus and profit sharing \
calculator. Please follow all data input guidelines for accurate calculations")


# Function contract
# Require argument match_t
# Print "Employee will recieve" match_t argument "etc..."
def contract(match_t):
    print("\nContract employee will recieve", match_t, "deposited into their \
profit sharing account")

# Function part_false
# Require argument match_f
# Print "Employee will recieve" match_f argument "etc..."
def part_false(match_f):
    print("\nEmployee is ineligible for a bonus, but", match_f, "will be \
deposited to the employee's profit sharing account")

# Function part_true
# Require argument bonus_t, match_t
# Print "Employee will recieve" bonus_t argument, "including..." match_t argument
def part_true(bonus_t, match_t):
    print("\nEmployee will recieve a bonus of", bonus_t, "plus a contribution \
of", match_t, "to their profit sharing account")

# Function full_false
# Require argument match_f, shares, share_value
# If employee owns shares, print "Employee ineligable for bonus but will recieve" 
#   match_f argument. "Employee owns" shares argument" worth shares*share_value
# Else print "Employee ineligable for bonus but will recieve" match_f argument
def full_false(match_f, shares, share_value):
    if shares >= 1:
        print("\nEmployee is ineligible for a bonus, but", match_f, "will be \
deposited to the employee's profit sharing account. \nEmployee is a private \
shareholder with", shares, "shares. Their inestment value of the comapny \
is", (shares * share_value))
    else:
        print("\nEmployee is ineligible for a bonus, but", match_f, "will be \
deposited to the employee's profit sharing account.")

# Function full_true
# Require argument bonus_t, match_f shares, share_value
# If employee owns shares, print "Employee is eligable for bonus and will recieve" 
#   bonus_t argument. "Employee will also recieve" match_t argument "Employee owns" 
#   shares argument "worth" shares*share_value
# Else print "Employee is eligable for bonus and will recieve" bonus_t argument. 
#   "Employee will also recieve" match_t argument 

def full_true(bonus_t, match_t, shares, share_value):
    if shares >= 1:
        print("\nEmployee will recieve a bonus of", bonus_t, "direct deposited \
to their bank account plus a contribution of", match_t, "to their profit sharing \
account. \nEmployee is a private shareholder with", shares, "shares. Their \
inestment value of the comapny is", (shares * share_value))
    else: 
        print("\nEmployee will recieve a bonus of", bonus_t, "direct deposited \
to their bank account plus a contribution of", match_t, "to their profit sharing \
account.")
#******************************************************************************

# Call eoy_bonus function to begin calculation
eoy_bonus()