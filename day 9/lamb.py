d=lambda x: x*2

print(d(5))

print(d(-3))

'''def do(x):
    x=x*2
    return x
print(do(5))'''


'''li=[5,4,3,2,6,8,98,45,66,9]
fli=list(filter(lambda x:(x%2!=0),li))
print(fli)'''


def alter(values,check):
    return [val for val in values if check(val)]

ml=[1,2,3,4,5]
ol=alter(ml,lambda x:x!=5)
print(ol)
    
f=list(filter(lambda x:(x!=5),ml))

print(f)



def alt(val,ch):
    return list(filter(ch,val))
ol=alt(ml,lambda x:x!=5)
print(ol)

#filter(expression/check condn,data)



x=input("Enter String ")
l=[]
for i in range(len(x)):
    l.append(x[i])
ln=list(filter(lambda x:not x.isdigit(),l))
xn=""
for i in range(len(ln)):
    xn=xn+ln[i]
print(xn)

