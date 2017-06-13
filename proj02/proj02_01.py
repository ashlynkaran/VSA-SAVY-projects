# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    # Calculates the year that the user will be 100
    year_100 = str((100 - age) + 2017)

else:
    # Calculates the year that the user will be 100
    year_100 = str((100 - age) + 2016)

print name, " will turn 100 in the year ", year_100, "."
