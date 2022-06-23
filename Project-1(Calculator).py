# Making a working calculator

# Making an input to select an option from the list

print("Press A for Addition")
print("")

print("Press S for Substraction")
print("")

print("Press M for Multipication")
print("")

print("Press DF for Division in Float")
print("")

print("Press DW for Division in Whole number")
print("")

print("If want to exit press any other letter")
print("")

Z=input("Enter your selection ==> ")
print("")
print("")

if Z=="A":
    print("Addition")
    print("")
    a=int(input("Enter a number ==> "))
    b=int(input("Enter another number ==> "))
    c=a+b
    print("")
    print("Addition of",a,"and",b,"is",c,)
    print("")
    print("THANK YOU")
    exit()
    
    
if Z=="S":
    print("substraction")
    print("")
    a=int(input("Enter a number ==> "))
    b=int(input("Enter another number ==> "))
    c=a-b
    print("")
    print("substraction of",a,"and",b,"is",c,)
    print("")
    print("THANK YOU")
    exit()
    

if Z=="M":
    print("Multiplication")
    print("")
    a=int(input("Enter a number ==> "))
    b=int(input("Enter another number ==> "))
    c=a*b
    print("")
    print("multipication of",a,"and",b,"is",c,)
    print("")
    
    print("THANK YOU")
    exit()
    
if Z=="DF":
    print("Division in Float")
    print("")
    a=int(input("Enter a number ==> "))
    b=int(input("Enter another number ==> "))
    c=a/b
    print("")
    print("Division of",a,"and",b,"is",c,)
    print("Remainder",c%10) # % 10 is used for getting the last digit we can even use it for getting last 2 digits using %100
    print("")
    print("THANK YOU")
    exit()
   
    
if Z=="DW":
    print("Division in Whole number")
    print("")
    a=int(input("Enter a number ==> "))
    b=int(input("Enter another number ==> "))
    c=a//b
    print("")
    print("Division of",a,"and",b,"is",c,)
    print("Remainder",c%10)
    print("")
    print("THANK YOU")
    exit()
   
    




