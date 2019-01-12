from tkinter import *
root=Tk()
btitle=Label(root,text="Title")
btitle.grid(row=0,column=0)

tentry=Entry(root)
tentry.grid(row=0,column=1)

bauthor=Label(root,text="Author")
bauthor.grid(row=0,column=2)

aentry=Entry(root)
aentry.grid(row=0,column=3)

byear=Label(root,text="Year")
byear.grid(row=1,column=0)

yentry=Entry(root)
yentry.grid(row=1,column=1)

bisbn=Label(root,text="ISBN")
bisbn.grid(row=1,column=2)

ientry=Entry(root)
ientry.grid(row=1,column=3)

l=Text(root,height=20,width=40)
l.grid(row=2,column=1)

b1=Button(root,text="View All")
b1.grid(row=2,column=3)

b2=Button(root,text="Search Entry",fg="red")
b2.grid(row=3,column=3)

b3=Button(root,text="Add Entry")
b3.grid(row=4,column=3)

b4=Button(root,text="Update Selected")
b4.grid(row=5,column=3)

b5=Button(root,text="Delete Selected")
b5.grid(row=6   ,column=3)
root.mainloop()