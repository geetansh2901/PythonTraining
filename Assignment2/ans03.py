i=input('Enter lower range limit:- ')
j=input('Enter upper range limit:- ')
k=input('Enter the number to be divided:- ')
i=int(i)
j=int(j)
k=int(k)
for i in range(i,j+1):
    if i%k is 0:
        print(i)