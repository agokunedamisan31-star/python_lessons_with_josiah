## This is my third python code.
## this is a conditional ccode that decide when one will be eligible to drive

my_age = int(input("Enter your age: "))
driver_license = True

if my_age <= 18:
    driver_license = False
    print("You can't drive now")
else:
    driver_license = True
    print("You can drive now")
