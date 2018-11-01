a=input('Enter the length of the first side of the triangle:- ')
a=float(a)
b=input('Enter the length of the second side of the triangle:- ')
b=float(b)
c=input('Enter the length of the third side of the triangle:- ')
c=float(c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is ',area)