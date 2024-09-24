def Calculator():
    num1=float(input("Enter Number one:"))
    operator= input("Enter the operator:")
    num2=float(input("Enter Number two:"))

    if operator=='+':
        result=num1+num2
        print(f"Addition of two numbers:{result:.2f}")

    elif operator=='-':
        result=num1-num2
        print(f"Subtraction of two numbers:{result:.2f}")

    elif operator=='*':
        result=num1*num2
        print(f"Multiplication of two numbers:{result:.2f}")

    elif operator=='/':
        result=num1/num2
        print(f"Division of two numbers:{result:.2f}")
    else:
        print("Operator is not available.")

Calculator()
                    
        