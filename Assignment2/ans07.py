a=input('Enter first number:- ')
a=int(a)
b=input('Enter second number:- ')
b=int(b)
c=input('Enter third number:- ')
c=int(c)
l=[]
for i in (a,b,c):
    l.append(i)
print(l)
for i in l:
    for j in l:
        for k in l:
            if i is not j and i is not k and j is not k:
                print('{}{}{}'.format(i,j,k))