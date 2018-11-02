a=input('Enter a number to check if its a pallindrome or not:- ')
a=int(a)
t=a
newno=0
newno=int(newno)
while a>0:
    k=int(a%10)
    newno=newno*10+k
    a=a//10
if t is newno:
    print('Number entered is pallindrome')
else:
    print('Number entered is not a pallindrome')