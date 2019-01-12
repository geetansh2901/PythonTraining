from tkinter import *
window=Tk()
l=Label(window,text="Fuck You...")
l.pack()
window.mainloop()
root=Tk()
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text="Button 1",fg="red")
button2=Button(topFrame,text="Button 2",fg="blue")
button3=Button(topFrame,text="Button 3",fg="green")
button4=Button(bottomFrame,text="Button 4",fg="purple")

#These buttons will be on top
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
#Button4 will be on bottom
button4.pack(side=BOTTOM)
root.mainloop()
'''

#FILL FUNCTION

root=Tk()
one=Label(root,text="one",bg="red",fg="blue")
one.pack()
two=Label(root,text="two",bg="black",fg="white")
two.pack(fill=X)
three=Label(root,text="three",bg="white",fg="purple")
three.pack(side=LEFT,fill=Y)
root.mainloop()'''