num1 = int(input("Enter num1(any integer) : "))
num2 = int(input("Enter num2(any integer except zero) : "))
operator = input("Enter arthmetic operation (+,-,*,/,%) : ")

s = {'+','-','*','/','%'}

if(operator not in s): print("Invalid operator")

while(operator not in s):
    operator = input("Enter arthmetic operation (+,-,*,/,%) : ")
    print("Invalid operator")

match operator:
    case '+':
        ans = num1+num2
        print(f"{num1} {operator} {num2} = {ans}")
    case '-':
        ans = num1-num2
        print(f"{num1} {operator} {num2} = {ans}")
    
    case '*':
        ans = num1*num2
        print(f"{num1} {operator} {num2} = {ans}")
    case '/':
        try:
            ans = num1/num2
            print(f"{num1} {operator} {num2} = {ans}")
        except ZeroDivisionError :
            print("can't divide by zero")
    case '%':
        ans = num1%num2
        print(f"{num1} {operator} {num2} = {ans}")
    
    case _:
        print("invalid operator")
    