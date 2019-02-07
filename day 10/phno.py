import re
'''x=input("Enter a phone number: ")
str=len(re.findall(r'\{3}-',x))
if str is 2 and len(x) is 12:
    print("valid")
else:
    print("invalid")'''

'''x=input("Enter full name: ")

str=len(re.findall(r'\s',x))
print(str)

if str>0:
    print("valid")
else:
    print("invalid")'''
    
x= input("Enter e-mail address: ")
if re.search(r"[\w._%+-]{1,20}@[\w.-]{2,20}.[a-z][A-Z]{2,3}",x):
   print("valid")
else:
    print("invalid")
    