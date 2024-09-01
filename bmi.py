# easy way code for bmi by python

weight = float(input("Enter your weight (by kilograms): ")) 
height = float(input("Enter your height (by meters): "))

bmi= weight/(height)**2 # This is your formule

print(f"Your Bmi {bmi}")

# now you must show to your user a result

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal")
elif 25 <= bmi < 29.9:
    print("Overweight")
elif 30 <= bmi < 34.9:
    print("Class 1 obesity")
elif 35 <= bmi < 39.9:
    print("Class 2 obesity")
else:
    print("Class 3 Obesity")

# now end :)
