from tkinter import *
def rightClick(event):
    l=Label(root,text="Right Click not allowed")
    l.grid(row=1,column=0)
root=Tk()

b1=Button(root,text="Print Message",command=rightClick)
b1.grid(row=0,column=0)
b1.bind("<Button-3>",rightClick)
b2=Button(root,text="Quit",command=root.quit)
b2.grid(row=0,column=1)

root.mainloop()