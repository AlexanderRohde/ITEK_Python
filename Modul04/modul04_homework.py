## Excercise 1 : Algorith Workbench.
#       n the table group do the “round table” and answer following questions. 3 Minutes preparation and 1 Minute presentation.

#1 Write a while loop that let the user enter a number. The number should be multiplied by 10, and  the result assigned to a variable named product. 
# The loop should iterate as long as product is less than 100. 

usernum = int(input("Numeral? "))
product = 0

while usernum < 100:
    usernum += product

# 2. Write a while loop that asks the user to enter two numbers. The numbers should be added and the  sum displayed. The loop should ask the user if he or she wishes to perform the operation again. If so, the loop should repeat, otherwise it should terminate.  

numb01 = int(input("Numeral? "))
numb02 = int(input("Numeral? "))
sum = numb01 + numb02
print(sum)

action = str(input("Type y to continue or n to end this cycle "))

while action != "y":
    pass

#3. Write a loop that uses the range function to display all odd numbers between 1 and 100. 



#4. Starting with a variable text containing an empty string, write a loop that prompts the user to type  a word. Add the users input to the end of text and the print the variable. The loop should repeat while the length of text is less than 10 characters. 

#5. Write a loop that calculates the total of the following series of numbers:  1/30 + 2/29 + 3/28 + ... 30/1 