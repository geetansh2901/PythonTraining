from func import *
c=input('Choose to calculate area of\n1.Triangle\n2.Circle ')
if c is '1':
    t=input('Do you want to enter base and height ')
    if t is 'y':
        b=input('Enter base ')
        h=input('Enter height ')
        b=float(b)
        h=float(h)
        tri(b,h);
    else:
        tri();
elif c is '2':
    t=input('Do you want to enter radius ')
    if t is 'y':
        r=input('Enter radius ')
        r=float(r)
        cir(r);
    else:
        cir();