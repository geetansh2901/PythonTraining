import math
from tkinter import *
root=Tk()
l=[]
def upd(n):
    l.append(n)
    if n is '=':
        l2=[]
        str=""
        for i in range(len(l)):
            if l[i] is '+' or l[i] is '-' or l[i] is '*' or l[i] is '/' or l[i] is '=':
                str=float(str)
                l2.append(str)
                l2.append(l[i])
                str=""
            else:
                str+=l[i]
        i=0
        while l2[i] is not '=':
            if l2[i] is '+':
                x=l2[i-1]+l2[i+1]
                print(x)
                del l2[0]
                del l2[0]
                l2[0]=x
                i=0
            elif l2[i] is '-':
                x=l2[i-1]-l2[i+1]
                print(x)
                del l2[0]
                del l2[0]
                l2[0]=x
                i=0
            elif l2[i] is '*':
                x=l2[i-1]*l2[i+1]
                print(x)
                del l2[0]
                del l2[0]
                l2[0]=x
                i=0
            elif l2[i] is '/':
                x=l2[i-1]/l2[i+1]
                print(x)
                del l2[0]
                del l2[0]
                l2[0]=x
                i=0
            i=i+1
        t.insert(END,l2[0])
    
    elif n is 'AC':
        
        i=len(l)-1
        del l[i]
        i=i-1
        while l[i].isdigit():
            del l[i]
            i-=1
    elif n is 'C':
        for i in range(0,len(l)):
            del l[0]
        print(l)
    elif n is 'sqrt':
        l3=[]
        str=""
        for i in range(len(l)):
            if l[i] is 'sqrt':
                str=float(str)
                l3.append(str)
                l3.append(l[i])
                str=""
            else:
                str+=l[i]
        print(l3)
        l3[0]=math.sqrt(l3[0])
        t.insert(END,l3[0])
        print(l3)
    elif n is 'sq':
        l3=[]
        str=""
        for i in range(len(l)):
            if l[i] is 'sq':
                str=float(str)
                l3.append(str)
                l3.append(l[i])
                str=""
            else:
                str+=l[i]
        print(l3)
        l3[0]=l3[0]*l3[0]
        t.insert(END,l3[0])
        print(l3)    
    elif n is '%':
        l2=[]
        str=""
        for i in range(len(l)):
            if l[i] is '+' or l[i] is '-' or l[i] is '*' or l[i] is '/' or l[i] is '%':
                str=float(str)
                l2.append(str)
                l2.append(l[i])
                str=""
            else:
                str+=l[i]
        print(l2)
        i=0
        while i is not '%':
            if l2[i] is '+':
                x=l2[i-1]+l2[i-1]*l2[i+1]/100
                print(x)
                t.insert(END, x)
            elif l2[i] is '-':
                x=l2[i-1]-l2[i-1]*l2[i+1]/100
                print(x)
                t.insert(END, x)
            elif l2[i] is '*':
                x=l2[i-1]*l2[i+1]/100
                print(x)
                t.insert(END, x)
            elif l2[i] is '/':
                x=l2[i-1]/(l2[i+1]/100)
                print(x)
                t.insert(END, x)
            i=i+1

def show(n):
    if n.isdigit() or n is '.':
        t.insert(END,n)
    elif n is 'AC':
        t.delete(1.0,END)
t=Text(root,height=1, width=8)
t.grid(row=1,column=8)
b7=Button(root,text="7",command= lambda: [show('7'),upd('7')]).grid(row=4,column=4)
b4=Button(root,text="4",command= lambda: [show('4'),upd('4')]).grid(row=5,column=4)
b1=Button(root,text="1",command= lambda: [show('1'),upd('1')]).grid(row=6,column=4)
b0=Button(root,text="0",command= lambda: [show('0'),upd('0')]).grid(row=7,column=4)

b8=Button(root,text="8",command= lambda: [show('8'),upd('8')]).grid(row=4,column=5)
b5=Button(root,text="5",command= lambda: [show('5'),upd('5')]).grid(row=5,column=5)
b2=Button(root,text="2",command= lambda: [show('2'),upd('2')]).grid(row=6,column=5)
bde=Button(root,text=".",command= lambda: [show('.'),upd('.')]).grid(row=7,column=5)

b9=Button(root,text="9",command= lambda: [show('9'),upd('9')]).grid(row=4,column=6)
b6=Button(root,text="6",command= lambda: [show('6'),upd('6')]).grid(row=5,column=6)
b3=Button(root,text="3",command= lambda: [show('3'),upd('3')]).grid(row=6,column=6)
bp=Button(root,text="%",command= lambda: [show('AC'),upd('%')]).grid(row=7,column=6)

ba=Button(root,text="+",command= lambda: [show('AC'),upd('+')]).grid(row=4,column=7)
bs=Button(root,text="-",command= lambda: [show('AC'),upd('-')]).grid(row=5,column=7)
bm=Button(root,text="*",command= lambda: [show('AC'),upd('*')]).grid(row=6,column=7)
bd=Button(root,text="/",command= lambda: [show('AC'),upd('/')]).grid(row=7,column=7)

bac=Button(root,text="AC",command= lambda: [show('AC'),upd('AC')]).grid(row=4,column=8)
# bbo=Button(root,text="(",command= lambda: [show('('),upd('(')]).grid(row=5,column=8)
bsr=Button(root,text="sqrt",command= lambda: [show('AC'),upd('sqrt')]).grid(row=6,column=8)
beq=Button(root,text="=",command= lambda: [show('AC'),upd('=')]).grid(row=7,column=8)

bc=Button(root,text="C",command= lambda: [show('AC'),upd('C')]).grid(row=4,column=9)
# bbc=Button(root,text=")",command= lambda: [show('('),upd('(')]).grid(row=5,column=9)
bsq=Button(root,text="^2",command= lambda: [show('AC'),upd('sq')]).grid(row=6,column=9)
root.mainloop()