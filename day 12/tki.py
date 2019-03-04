
from tkinter import *
window=Tk()
def kmtom():
    print(e1_value.get())
    m=float(e1_value.get())*0.62137
    t1.insert(END, m)
b1=Button(window,text='Calculate',command=kmtom)
#b1.pack()
b1.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)
window.mainloop()
