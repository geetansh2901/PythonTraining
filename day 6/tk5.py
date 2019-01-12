from tkinter import *
root=Tk()
logo=PhotoImage(file="Capture.png")
w1=Label(root,image=logo).pack(side="right")
explanation="Fuck Online Transactons"

w2=Label(root,justify=LEFT,padx=10,text=explanation).pack(side="left")
root.mainloop()