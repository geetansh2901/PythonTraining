a=input('Enter a number to find its reverse:- ')
a=int(a)
newno=0
newno=int(newno)
while a>0:
    k=int(a%10)
    newno=newno*10+k
    a=a//10
print('After reversing the number:- ',newno)