#Ask the user for a start value
startvalue = int(input("Please type in a start value "))
#Ask the user for an end value
endvalue = int(input("Please type in end value " ))
#Ask the user for a step value
stepvalue = int(input("Please type in step value "))
#Print out the number from ‘start’ to ‘end’ in ‘steps’ using a for loop with range

for x in range(startvalue,endvalue,stepvalue):
    print(x)