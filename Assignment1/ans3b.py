a=input('Enter the value of a:- ')
b=input('Enter the value of b:- ')
a=int(a)
b=int(b)
print('Before swapping, the value of a is {} and value of b is {}'.format(a,b))
a=a+b
b=a-b
a=a-b
print('After swapping, the value of a is {} and value of b is {}'.format(a,b))