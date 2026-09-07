# ShadowFox - Beginner Task 3
# Section: Lists

# Justice League initial list

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]
# Question 1: Calculate the number of members in the Justice League

print("Q1 - Number of members:", len(justice_league))

# Question 2: Add Batgirl and Nightwing to the list

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

# Question 3: Wonder Woman is the leader.
# Move her to the beginning of the list.

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("Q3 - After moving Wonder Woman to the beginning:")
print(justice_league)



print("Q5 - New Justice League:")
print(justice_league)


# Question 6:
# Sort the Justice League alphabetically.
# The hero at index 0 becomes the new leader.

justice_league.sort()

print("Q6 - Alphabetically sorted Justice League:")
print(justice_league)

print("New leader:", justice_league[0])

# Question 4 : Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.

# Q4
# Move Green Lantern between Aquaman and Flash

justice_league.remove("Aquaman")
justice_league.remove("Green Lantern")

flash_index = justice_league.index("Flash")

justice_league.insert(flash_index, "Aquaman")
justice_league.insert(flash_index + 1, "Green Lantern")

print("Q4 - After separating Aquaman and Flash:")
print(justice_league)