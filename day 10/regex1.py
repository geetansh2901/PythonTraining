import re
'''NameAge="Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21"
ages=re.findall(r'\d{1,3}',NameAge)
names=re.findall(r'[A-Z][a-z]*',NameAge)
a={}
x=0
for name in names:
    a[name]=ages[x]
    x+=1
print(a)

'''

'''import re
allinform=re.findall("inform","we need to inform him with the latest information")
print(allinform)'''

'''Str="we need to inform him with the latest information"
for i in re.finditer("inform",Str):
    loc=i.span()
    print(loc)'''
    
'''s="Sat,hat,mat,pat"
alls=re.findall("[shmp]at",s)
print(alls)
for i in alls:
    print(i)'''
    
''''s="Sat,hat,pat,mat"
alls=re.findall("[h-m]at",s)
print(alls)'''
    
    
'''s='hat mat rat pat'
regex=re.compile("[r]at")
print(regex)
s=regex.sub("food",s)
print(s)'''

'''rands="12345"
print("Matches:",len(re.findall("\d{5}", rands)))
print(re.findall("\d{5}",rands))'''

str="""
hello i am
 nishant
 whats up!!"""
print(str)

regex=re.compile("\n")
str=regex.sub('',str)
print(str )

str2='here is \\bpit'
print(str2)
print(re.search(r'\\bpit',str2))