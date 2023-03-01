import math

radius = float(input("Choose the radius of a circle "))

areal = math.pi * pow(radius, 2)
omkreds = 2 * math.pi * radius

print(areal)
print(omkreds)

print(math.ceil(areal))
print(math.ceil(omkreds))
