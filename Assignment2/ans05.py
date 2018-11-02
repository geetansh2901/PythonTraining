marks=[]
i=0
i=int(i)
avg=0
for i in range(5):
    x=input('Enter marks in subject{}:- '.format(i+1))
    x=int(x)
    marks.append(x)
    avg+=x/5
if avg>=90:
    print('Grade: A')
elif avg<90 and avg>=80:
    print('Grade: B')
elif avg>=70 and avg<80:
    print('Grade: C')
else:
    print('Grade: D')