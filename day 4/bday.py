from calendar import *
from datetime import *
'''class bday():
    def __init__(self):
        self.dat=int(input('Enter date'))
        self.mon=int(input('Enter month'))
        self.yr=int(input('Enter year'))
        self.hr=int(input('Enter hour'))
        self.min=int(input('Enter minutes'))
        self.sec=int(input('Enter seconds'))
        self.mls=int(input('Enter milliseconds'))
        self.mcs=int(input('Enter microsecond'))
x=bday()
y=datetime(x.yr, x.mon, x.dat, x.hr,x.min)'''
y=datetime(1998,1,29,12,28)
print(y)
delta=datetime.now()-y
print(delta)
x=delta.days
print('{} weeks and {} days '.format(x//7,x%7))
years=(x)//365#finding years
print(years,'years')
montd=x-20*365#finding days of the current year
print(montd)
months=0
for i in [31,28,31,30,31,30,31,31,30,31,30,31]:#finding months
    montd-=i
    months+=1
    if montd<30:
        break
for i in range(1998,2018):# subtracting extra days of leap year
    if i%4 is 0:
        montd-=1
print(montd,'days')

print('Age is {} years, {} months and {} days or {}'.format(years,months,montd,delta))
