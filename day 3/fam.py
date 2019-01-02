'''enter family details
name and age            
two having same age  condition
enter name and find age 
min 5 '''

m=dict()
print(m)
for i in range(5):
    x=input('Enter name:-')
    y=input('Enter age:-')
    y=int(y)
    m[i]=dict(name=x,age=y)
print(m)
x=input('Enter name of the person whose age is to be found:-')
a=1000
for i in range(5):
    d=m[i]
    print(d)
    if d['name'] is x:
        a=d['age']
        print(a)
for i in range(5):
    d=m[i]
    if d['age'] is a and d['name'] is not x:
        print('There is also a person with same age:-',d['name'])
        