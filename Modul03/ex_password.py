age = int(input("Age please "))
psw = str(input("Please enter your password "))
threshold = 20
upsw = "JonBonesJones123"
if age > threshold and psw == upsw :
    print("You have been granted access")
elif age < threshold: print(age)
elif psw != upsw: print("password does not match what is on file: " + psw)