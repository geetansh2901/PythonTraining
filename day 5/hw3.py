from tkinter import *
window=Tk()
def kgtg():
    print(e1_value.get())
    g=float(e1_value.get())*1000
    t1.insert(END,g)
def kgtp():
    p=float(e1_value.get())*2.20462
    t2.insert(END,p)
def kgtoz():
    o=float(e1_value.get())*35.274
    t3.insert(END,o)
b1=Button(window,text='Convert',command=lambda:[kgtg(),kgtp(),kgtoz()])
b1.grid(row=0,column=2)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
labelText=StringVar()
labelText.set("Kilograms")
labelDir=Label(window, textvariable=labelText, height=4)
labelDir.grid(row=0,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)
labelText1=StringVar()
labelText1.set("Grams")
labelDir=Label(window, textvariable=labelText1, height=4)
labelDir.grid(row=2,column=0)
labelText2=StringVar()
labelText2.set("Pounds")
labelDir=Label(window, textvariable=labelText2, height=4)
labelDir.grid(row=2,column=1)
labelText3=StringVar()
labelText3.set("Ounces")
labelDir=Label(window, textvariable=labelText3, height=4)
labelDir.grid(row=2,column=2)
window.mainloop()