# 45*3 - 555, 56+9 - 77, 56/6 - 4
print("Enter num1")
num1 = int(input())
print("Enter num2")
num2 = int(input())
print("Enter your Operator(+,-,/,%,*)")
num3 = input()
if num1==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1==56 and num2==6 and num3=='/':
    print("4")
elif num3=='+':
    print(num1+num2)
elif num3=='-':
    print(num1-num2)
elif num3=='*':
    print(num1*num2)
elif num3=='/':
    print(num1/num2)
elif num3=='%':
    print(num1%num2)
