
# ShadowFox Python Development Internship
# Beginner Task - For Loop


# Question 1: Six-Sided Dice Simulation

import random

six_count = 0
one_count = 0
two_six_in_row = 0
previous_roll = 0

for i in range(20):
    roll = random.randint(1, 6)

    print("Roll", i + 1, ":", roll)

    # Count how many times 6 was rolled
    if roll == 6:
        six_count += 1

    # Count how many times 1 was rolled
    if roll == 1:
        one_count += 1

    # Check whether two 6s were rolled consecutively
    if previous_roll == 6 and roll == 6:
        two_six_in_row += 1

    previous_roll = roll


print("\nDice Statistics")
print("Number of 6s:", six_count)
print("Number of 1s:", one_count)
print("Two 6s in a row:", two_six_in_row)



# Question 2: 100 Jumping Jacks


completed_jacks = 0

for i in range(10):

    completed_jacks += 10

    print("\nYou completed", completed_jacks, "jumping jacks.")

    if completed_jacks == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":

        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed_jacks, "jumping jacks.")
            break

        elif skip == "no" or skip == "n":
            remaining = 100 - completed_jacks
            print(remaining, "jumping jacks remaining.")

    elif tired == "no" or tired == "n":
        remaining = 100 - completed_jacks
        print(remaining, "jumping jacks remaining.")