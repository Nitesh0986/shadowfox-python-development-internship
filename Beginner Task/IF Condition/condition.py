# ShadowFox - Beginner Task 4
# Section: IF Condition

# Question 1: BMI Category

#Write a program to determine the BMI Category based on user input.

#Ask the user to:

#Enter height in meters
#Enter weight in kilograms
#Calculate BMI using the formula:
#BMI = weight / (height)²

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

BMI = weight / (height ** 2)

print("BMI:", BMI)

if BMI >= 30:
    print("Obesity")

elif 25 <= BMI < 30:
    print("Overweight")

elif 18.5 <= BMI < 25:
    print("Normal")

else:
    print("Underweight")

# Question 2 : check if a city is in UAE
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]

a = input("Enter a city name: ")

if a in UAE:
    print(a, "is in UAE")

# Question 3 : same country
# Given two cities, write a program to check whether they belong to the same country.

#Use these lists:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]

UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

elif city1 in India and city2 in India:
    print("Both cities are in India")

else:
    print("Both cities are not in the same country")