''''a='GeetAnsh'
b=a.capitalize()
print(b)

b=a.replace('A','a')
print(b)
'''
# skip character from string

x=input("Enter String ")
y=input("Enter character to remove")
l=[]
for i in range(len(x)):
    l.append(x[i])
ln=list(filter(lambda x: x is not y,l))
xn=""
for i in range(len(ln)):
    xn=xn+ln[i]
print(xn)