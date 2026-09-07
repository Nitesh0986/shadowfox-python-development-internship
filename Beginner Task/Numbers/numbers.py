# ShadowFox - Beginner Task 2
# Section: Numbers

# Question 1 : Use the format() function with 145 and 'o'.
# 'o' represents octal representation.


def format_number(number, representation):
    return format(number, representation)


result = format_number(145, 'o')

print("Formatted value:", result)
#Output : Formatted value: 221

#Question 2: Calculate the area of a circular pond.
radius = 84 
pi = 3.14
area = pi * radius ** 2
print("Area of the circular pond:", area) #22155.84

# Bonus Question :  1.4 liters of water per square meter
water_per_square_meter = 1.4

total_water = area * water_per_square_meter

print("Total water:", int(total_water)) #31018

# Question 3:  Calculate speed in meters per second.
distance = 490
time = 7

time_seconds = time * 60

speed = distance / time_seconds
print("Speed in meters per second:", int(speed)) #1