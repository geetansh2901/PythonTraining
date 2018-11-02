n=input('Enter how many number you want to enter:- ')
n=int(n)
i=0
i=int(i)
l=[]
for i in range(n):
    x=input('Enter number:- ')
    x=float(x)
    l.append(x)
j=0
sum=0
for j in range(n):
    sum+=l[j]
print('Average of the numbers entered:- ',sum/n)
print(l)