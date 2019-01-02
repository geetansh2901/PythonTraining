'''def printa(str):
    print(str)

printa('Faggot')'''

'''
PASS BY REFERENCE

def changeme(mylist):
    mylist.append([1,2,3,4])
    print('Values inside the function  ',mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print('Values outside the function ',mylist)#nested list
'''
'''
PASS BY VALUE

def changeme(mylist):
    mylist=[1,2,3,4]
    print('Inside ',mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print('Outside ',mylist)'''

# KEYWORD ARGUMENTS

'''def area(l,b):
    area1=0.5*l*b
    area2=l*b
    return area1,area2'''

'''def area(l,b):
    print('l= ',l)
    print('b= ',b)
    area1=0.5*l*b
    area2=l*b
    return area1,area2
a=area(b=4,l=5)
print('Area of tri : ',a[0])
print('Area of rec : ',a[1])
print(a)'''

#DEFAULT ARGUMENTS'

'''def area(l=6,b=10):
    print('l= ',l)
    print('b= ',b)
    area1=0.5*l*b
    area2=l*b
    return area1,area2
a=area()
print('Area of tri : ',a[0])
print('Area of rec : ',a[1])
print(a)

'''


#AREA FUNCTION  CHOOSE TO CALCULATE AREA 1.TRIANGLE 2. CIRCLE

from math import *
def tri(b=0,h=0):
    area=0.5*b*h
    print('Area of the triangle is ',area)
def cir(r=0):
    area=pi*r*r
    print('Area of the circle is ',area)