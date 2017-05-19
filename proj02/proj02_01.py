# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


# Asks user to enter name
raw_name = raw_input("Enter your first name: ")

# Formats name
name = raw_name[0].upper() + raw_name[1:].lower()

# Asks user to enter age
age = int(raw_input("Enter your age: "))

if age < 100:
    old = False
else:
    old = True

# Ask user whether they have had a birthday this year
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    # Calculates the year that the user will be 100
    year_100 = str((100 - age) + 2017)
    valid = True
elif birthday == "N":
    # Calculates the year that the user will be 100
    year_100 = str((100 - age) + 2016)
    valid = True
else:
    valid = False

# Prints message about year that user turns 100
if valid and old:
    print(name + " turned 100 in the year " + year_100 + "!")
elif valid:
    print (name + " will turn 100 in the year " + year_100 + "!")
else:
    print("Invalid input.")

# Prints message about movies that user can watch
if age < 13:
    print (name + " can watch G or PG movies.")
elif age < 17:
    print (name + " can watch G, PG, or PG-13 movies.")
else:
    print (name + " can watch G, PG, PG-13, or R movies.")
