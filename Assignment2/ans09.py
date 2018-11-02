a=input('Enter a number to find the number of digits:- ')
a=int(a)
sum=0
while a>0:
    sum+=1
    a=a//10
print('Number of digits:- ',sum)