from tkinter import *
def log():
    l=Label(root,text="You are logged in")
    l.grid(columnspan=3)
root=Tk()
l1=Label(root,text="Name")
l2=Label(root,text="Password")
e1=Entry(root)
e2=Entry(root)

#widgets centered by default, sticky option to chnage
l1.grid(row=0,sticky=E)
l2.grid(row=1,sticky=E)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

#widgets can take up more than one cell with columnspan and rowspan
c=Checkbutton(root,text='Keep me logged in',command=log)
c.grid(columnspan=2)
b1=Button(root,text="Quit",command=root.quit)
b1.grid(row=3,column=0)
root.mainloop()