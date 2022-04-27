
def calculate_F():
    wind_chill_F = 35.74 + (0.6215*temp) - (35.75*(v**0.16)) + (0.4275*(temp*(v**0.16)))    
    return wind_chill_F

def calculate_C():
    temp_C = float(temp * (9/5) + 32)
    wind_chill_C = 35.74 + (0.6215*temp_C) - (35.75*(v**0.16)) + (0.4275*(temp_C*(v**0.16)))    
    return wind_chill_C

v = 5
temp = float(input("What is the temperature? "))
scale = input("Fahrenheit or Celsius (F/C)? ")


while v <= 60:
    if scale.lower() == "f":
        print(f"At temperature {temp}F, and wind speed {v} mph, the windchill is: {calculate_F():.2f}F")
        
    if scale.lower() == "c":
            print(f"At temperature {float(temp * (9/5) + 32):.1f}F, and wind speed {v} mph, the windchill is: {calculate_C():.2f}F")

    v += 5


