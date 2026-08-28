# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0

# Put your code below
# days = 86400
# hours = 3600
# minutes = 60
input_int = int(input_str)
num_days = input_int // 86400
input_int %= 86400
num_hours = input_int // 3600
input_int %= 3600
num_minutes = input_int // 60
num_seconds = input_int % 60



################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')