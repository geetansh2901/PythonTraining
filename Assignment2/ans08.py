a=input('Enter a number to find the sum of its constituent numbers:- ')
a=int(a)
sum=0
while a>0:
    k=int(a%10)
    sum+=k
    a=a//10
print('Sum of the number:- ',sum)