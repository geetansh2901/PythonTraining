n=input('Enter upto how many terms you want the sum of natural numbers:- ')
n=int(n)
l=[]
sum=0
for i in range(1,n+1):
    sum+=i
    l.append(i)
print(l[0],end='')
for i in range(1,n):
    print('+',l[i],end='')
print('=',sum)