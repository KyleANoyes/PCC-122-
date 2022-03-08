#******************************************************************************
# Author:           Kyle Noyes
# Lab:              Lab 4
# Date:             2/27/2022
#
# Description:      This program calculates what the end of year bonus amount
#                   and contributions to employee'sprofit sharing accounts will 
#                   be and if they are eligable for a bonus or not. 
#
# Input:            Program first seeks the type of employment, pay, number of
#                   hours worked since Jan 1st, and base company contributions.
#
# Output:           Whether the employee is eligible for a bonus or not alongside 
#                   employee specific information. Additionally, the bonus / employee 
#                   match contribution amount will be displayed
#
# Alterations:      This code has now been refined to never allow bad user input.
#                   While the values inputed are not complex, one single bad data
#                   entry will completely break this program. The new verions for
#                   Lab 4 now incorporates both Try/Except and While loops that
#                   work in tandem to never let a user input bad data and to 
#                   defensively re-promprt them for correct data formats.
#
# Sources:          Lab 3/4 specifications and video. Also a downright unhealthy 
#                   amount of research/staring at stack overflow           
#******************************************************************************

# Validation checking - High priority for all data to be valid to avoid errors
#
# floatvalid function will test if numerical data is inputted correctly
# Recieve function call with user data, assigne data as temp value "i"
# test if "i" is a float
# if "i" is a float, then the data is a known good entry
# return "True" 
# if "i" is not a float, invalid data input was inputer and needs to be discarded
# return "Flase"

def floatvalid(i):
    try:
        i = float(i)
        return True
    except:
        print("Unknown input, please enter a valid number. \nExample: 31.25 for $31.25/hr")
        return False

# empvalid function will test if employee status was inputted correctly
# Recieve function call with user data, assigne data as temp value "i"
# test if "i" is an int
# if "i" is an int, then test what that int is
# test if "i" is equal to 1, 2, or 3. If so then return "True"
# if "i" does not equal 1, 2, or 3, then return "False"
# if "i" is not an int, invalid data input was inputer and needs to be discarded
# return "Flase"

def empvalid(i):
    try: 
        i = int(i)
        if i == 1 or i == 2 or i == 3:
            return True
        else:
            print("Incorrect entry, please input employee type again. 1, 2, or 3")
            return False
    except:
        print("Unknown or invalid input detected, please re-input data.")
        return False


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
#
# validation rules: status must always be equal to 1, 2, or 3
# Call function empvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_status():
    while True:
        status = 0
        status = (input("\nPlease enter the employee's type of employment. \
Contractor = 1, Regular part-time = 2, Regular full-time = 3: "))
        entry = empvalid(status)
        if entry == False:
            continue
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
#
# validation rules: user input must be a float or int value
# Call function floatvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_rate():
    while True:
        rate = 0.00
        rate = (input("\nPlease enter the employee's hourly pay rate: "))
        entry = floatvalid(rate)
        if entry == True:
            rate = float(rate)
            return rate
        else:
            continue

# Function get_hours
# Set hours = 0
# Ask user to input number of hours worked this year
# Truncate value down to single digit
# return hours = truncated user input
#
# validation rules: user input must be a float or int value
# Call function floatvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_hours():
    while True:
        hours = 0
        hours = (input("\nPlease input how many hours this employee has worked \
from since January 1'st of this year: "))
        entry = floatvalid(hours)
        if entry == True:
            hours = float(hours)
            return hours
        else:
            continue

# Function get_contribute
# Set contribute = 0
# Ask user to input the company profit sharing match %
# Return hours = user inputed float/int
#
# validation rules: user input must be a float or int value
# Call function floatvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_contribute():
    while True:
        contribute = 0
        contribute = (input("\nPlease enter the profit share percnatage \
contribution from employee's wage (5% = 0.05): "))
        entry = floatvalid(contribute)
        if entry == True:
            contribute = float(contribute)
            return contribute
        else:
            continue

# Function get_shares
# Set shares = 0
# Ask user to input the number of shares held by employee
# Return shares = user inputed float/int
#
# validation rules: user input must be a float or int value
# Call function floatvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_shares():
    while True:
        shares = 0
        shares = (input("\nPlease state number of shares owned by employee: "))
        entry = floatvalid(shares)
        if entry == True:
            shares = float(shares)
            return shares
        else:
            continue

# Function get_share_value
# Set value = 0
# Ask user to input the value of a single share
# Return value = user inputed float/int
#
# validation rules: user input must be a float or int value
# Call function floatvalid with user input as argument
# get boolean operator of validation checker
# if false, reset this function to base values and prompt user for new input
# if true, data is valid and can be used in the program

def get_share_value():
    while True:
        value = 0
        value = (input("\nPlease input the value of a single share: "))
        entry = floatvalid(value)
        if entry == True:
            value = float(value)
            value = value // 0.01
            return value
        else:
            continue
    

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