import sqlite3 as sq
from tkinter import *
conn=sq.connect("book.db")
cursor=conn.cursor()
#cursor.execute("CREATE TABLE boo(num INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT, author TEXT, year INTEGER, isbn INTEGER);")
def view():
    cursor.execute("SELECT * FROM boo;")
    l=cursor.fetchall()
    t.delete(0,len(l))
    for r in l:
        t.insert(END,r)

def ins():
    cursor.execute("INSERT INTO boo VALUES(NULL,?,?,?,?)",(tit.get(),aut.get(),yr.get(),isb.get()))
    conn.commit()   

def sear():
    cursor.execute("SELECT * FROM boo WHERE title=? OR author=? OR year=? OR isbn=?;",(tit.get(),aut.get(),yr.get(),isb.get()))
    l=cursor.fetchall()
    t.delete(0,len(l))
    for r in l:
        t.insert(END,r)
    
def upd():
    l=list(t.get(ACTIVE))
    print(l)

    cursor.execute("UPDATE boo SET title=?, author=?, year=?, isbn=? where num=?;",(tit.get(),aut.get(),yr.get(),isb.get(),l[0]))
    conn.commit()

    
def dee():
    l=list(t.get(ACTIVE))
    l[0]=str(l[0])
    cursor.execute("DELETE FROM boo WHERE num=?;",(l[0]))
    conn.commit()













root=Tk()
tit=StringVar()
l1=Label(root,text="Title").grid(row=0,column=3)
e1=Entry(root,textvariable=tit).grid(row=0,column=5)
aut=StringVar()
l2=Label(root,text="Author").grid(row=0,column=7)
e2=Entry(root,textvariable=aut).grid(row=0,column=9)
yr=IntVar()
l3=Label(root,text="Year").grid(row=2,column=3)
e3=Entry(root,textvariable=yr).grid(row=2,column=5)
isb=IntVar()
l4=Label(root,text="ISBN").grid(row=2,column=7)
e4=Entry(root,textvariable=isb).grid(row=2,column=9)
t=Listbox(root,height=10,width=60)
t.grid(row=4,column=6)
#t.insert(END,"Geetansh")
b1=Button(root,text="Search Entry",command=sear,bg="black",fg="white").grid(row=9,column=6)
b2=Button(root,text="Add Entry",command=ins,bg="white",fg="blue").grid(row=10,column=6)
b3=Button(root,text="Update Selected",command=upd,bg="brown",fg="yellow").grid(row=11,column=6)
b4=Button(root,text="Delete Selected",command=dee,bg="lime",fg="purple").grid(row=12,column=6)
b5=Button(root,text="View All",command=view,bg="yellow").grid(row=13,column=6)
b6=Button(root,text="Exit",command=root.quit,bg="blue",fg="lime").grid(row=14,column=6)
root.mainloop()