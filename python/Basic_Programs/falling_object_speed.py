# Task: Determine how fast an object will fall

import math

# print("Welcome to the velocity calculator.  Please enter the following: ")

# m = float(input("Mass (in kg): "))
# g = float(input("Gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): "))
# t = float(input("Time (in Seconds): "))
# p = float(input("Density of the fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): "))
# A = float(input("Cross sectional area of projectile (in square meters): "))
# C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# c = (1 / 2) * p * A * C
# v = math.sqrt((m*g)/c) * (1 - math.exp((-math.sqrt (m * g * c) / m) * t))

# print(f"\nThe inner value of C is : {c:.3f} ")
# print(f"the velocity after 10.0 seconds is: {v:.3f} m/s \n")


# Stretch Challenges:

print("\nNow let's calculate the velocity of a bowling ball: ")

m = float(input("\nMass of the bowling ball (in kg): "))
t = float(input("Time (in Seconds): "))
p = float(input("Density of the fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): "))
r = float(input("Radius of the bowling ball (in cm): "))

g_earth = 9.8
g_jupiter = 24
C = 0.5
A = math.pi * ((r/100) ** 2)

c = (1 / 2) * p * A * C


v_earth = math.sqrt((m*g_earth)/c) * (1 - math.exp((-math.sqrt (m * g_earth * c) / m) * t))
v_jupiter = math.sqrt((m*g_jupiter)/c) * (1 - math.exp((-math.sqrt (m * g_jupiter * c) / m) * t))

print(f"\n\nThe Velocity of the bowling ball on earth is {v_earth:.3f} m/s \n")
print(f"The Velocity of the bowling ball on Jupiter is {v_jupiter:.3f} m/s \n")


