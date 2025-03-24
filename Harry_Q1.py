while True:
    print("Enter two values")
    a = float(input())
    b = float(input())
    while a/a!=1 and b/b==1:
        print("Please input integer numbers")
        a = float(input())
        b = float(input())
    print("The input numbers are",a,"and",b)
    print("Enter the operation you want to perform")
    c = input()
    while c != "+" and c != "-" and c != "*" and c != "/":
        print("The operation you entered is invalid.\nPlease enter between +,-,*,/")
        c = input()

    if c == "+":
        print("The sum of the two values are", a + b)
    elif c == "-":
        print("The substraction of the two values are", a - b)
    elif c == "*":
        print("The multiplication of the two values are", a * b)
    elif c == "/":
        if b == 0:
            print("This operation is invalid\nYou can't divide a number by 0")
        else:
            print("The divided value is ",a/b)
