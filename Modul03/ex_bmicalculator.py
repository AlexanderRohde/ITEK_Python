weight = float(input("Weight in kg? "))
height = float(input("Height in m?(1.5  or 1.8 etc) "))

bmi = weight/pow(height, 2)
print(bmi)

if bmi < 18.5:
    print("Thin")
elif bmi < 25 and bmi >= 18.5:
    print("Healthy")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
