print('this is print function')
a=6
print('The value of a is ',a)

print('Enter value of a: ',end='')
a=input('-------')
print(a)


print('Enter value','of a is ',sep='+',end='\n')
a=input()
print(a)


x=5
y=9
print('The value of x is {} and y is {}'.format(x,y))
print('The value of x is {1} and y is {0}'.format(x,y))
#or print('The value of x is {} and y is {}'.format(y,x))