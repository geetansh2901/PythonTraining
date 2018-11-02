n=input('Enter the order of identity matrix to be printed:- ')
n=int(n)
for i in range(n):
    print()
    for j in range(n):
        if i is j:
            print('1\t',end='')
        else:
            print('0\t',end='')