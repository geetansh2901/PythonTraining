'''d={'name':'faggot','id':33}
print(d)
d1=dict(name='Dick Sucker',gender=3)
print(d1)'''

d=dict(one=1,two=2,three=3)
print(d)
for k in d:
    print(k,d[k])
for k in sorted(d.keys()):
    print(k,d[k])
    
for k,v in sorted(d.items()):
    print(k,v)
    
for v in sorted(d.values()):
    print(v)
for k in d:
    print(k)
d['seven']=7
s=d.get('threer','Key not found')
print(s)

c=d.pop('one1','Key not found')
print(c)

del d['two']
print(d)

x=dict(uno=1,dos=2,tres=3,**d)
print(x)