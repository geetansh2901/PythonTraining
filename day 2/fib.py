first=0
second=1
n=input('Enter upto how many terms you want to print fibonacci series ');
n=int(n)
i=0
print(first)
print(second)
for i in range(n):
    sum=first+second
    print(sum)
    first=second
    second=sum