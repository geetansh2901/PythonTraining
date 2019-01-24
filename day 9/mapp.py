l=[5,7,22,97,54,62]
fl=list(map(lambda x: x*2,l))
print(fl)
from functools import reduce

sum=reduce((lambda x,y:x+y),l)
print(sum)