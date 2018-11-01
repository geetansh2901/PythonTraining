a=input('Enter the first number:- ')
a=float(a)
s=input('Enter one of the arithematic operation to be performed:- ')
b=input('Enter the second number:- ')
b=float(b)
if s is '+':
    print('Result:- ',a+b)
elif s is '-':
    print('Result:- ',a-b)
elif s is '*':
    print('Result:- ',a*b)
elif s is '/':
    print('Result:- ',a/b)