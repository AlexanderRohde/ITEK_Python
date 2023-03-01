#Exercise - Time Calculator
#Write a program that asks the user to enter a number of 
# seconds and works as follows:

#There are 60 seconds in a minute. If the number of seconds
# entered by the user is greater than or equal to 60,
# the program should convert the number of seconds to minutes and seconds.

#There are 3600 second in an hour. If the number of seconds entered by the user is greater than or
#equal to 3600, the program should convert the number of seconds to hours, minutes and seconds.

#There are 86400 seconds in a day. If the number of seconds entered by the user is greater than or
#equal to 86400, the program should convert the number of seconds to days, hours, minutes and
#seconds.

# day/secs = antal dage, (24 hours pr d)
# hour/secs = antal timer (60 min pr hour)
# min/secs = antal min (60 sek pr min)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

secs = int(input("Pick a number above 60"))
print(convert(secs))