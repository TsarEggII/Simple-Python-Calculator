Welcome = input("Welcome to calculator, press any button, and then enter to continue!")
Option = input("Do you want arithmetic or comparison?")
if(Option == "arithmetic"):
    x = int(input("What is your first integer?"))
    Operator = input("What is your operator, choose from: +,-,/,*,//,**,%")
    y = int(input("What is your second integer?"))

    if(Operator == "+"):    
        print("You chose summation, here is your result!")
        print(x + y)


    if(Operator == "-"):
        print("You chose subtraction, here is your result!")
        print(x - y)


    if(Operator == "*"):
        print("You chose multiplication, here is your result!")
        print(x * y)


    if(Operator == "/"):
        print("You chose division, here is your result!")
        print(x / y)


    if(Operator == "//"):
        print("You chose quotient, here is your result!")
        print(x // y)


    if(Operator == "**"):
        print("You chose exponent, here is your result!")
        print(x ** y)


    if(Operator == "%"):
        print("You chose remainder, here is your result!")
        print(x % y)

if(Option == "comparison"):
    z=int(input("What is your first integer?"))
    Comparison=input("What comparison do you want? <,>,==,<=,>=,!=")
    w=int(input("What is your second integer?"))

    if(Comparison == "<"):
        print("You chose <")
        print(z < w)

    if(Comparison==">"):
        print("You chose >")
        print(z > w)

    if(Comparison=="=="):
        print("You chose ==")
        print(z == w)

    if(Comparison=="<="):
        print("You chose <=")
        print(z <= w)

    if(Comparison==">="):
        print("You chose >=")
        print(z >= w)

    if(Comparison=="!="):
        print("You chose !=")
        print(z != w)

