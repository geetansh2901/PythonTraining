def connect1():
    
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE lakshya(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, aim TEXT);")
def insert1():
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()    
    x=input('Enter Name: ')
    y=int(input('Enter Age: '))
    z=input('Enter Aim: ')
    cursor.execute("INSERT INTO lakshya VALUES(NULL,?,?,?);",(x,y,z))
    conn.commit()
def update2():
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()
    x=input('Enter what do you want to update :\n1.Name\n2.Age\n3.Aim\nEnter choice(1/2/3)')
    x1=input('Enter update value')
    y=input('Enter what information you have :\n1.Name\n2.Age\n3.Aim\nEnter choice(1/2/3)')
    y1=input('Enter information value')
    if x is '1':
        if y is '1':
            cursor.execute("UPDATE lakshya SET name=? where name=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '2':
            y1=int(y1)
            cursor.execute("UPDATE lakshya SET name=? where age=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '3':
            cursor.execute("UPDATE lakshya SET name=? where aim=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
    elif x is '2':
        x1=int(x1)
        if y is '1':
            cursor.execute("UPDATE lakshya SET age=? where name=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '2':
            y1=int(y1)
            cursor.execute("UPDATE lakshya SET age=? where age=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '3':
            cursor.execute("UPDATE lakshya SET age=? where aim=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
    elif x is '3':
        if y is '1':
            cursor.execute("UPDATE lakshya SET aim=? where name=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '2':
            y1=int(y1)
            cursor.execute("UPDATE lakshya SET aim=? where age=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
        if y is '3':
            cursor.execute("UPDATE lakshya SET aim=? where aim=?;",(x1,y1))
            cursor.execute("SELECT * FROM lakshya;")
            print(cursor.fetchall())
    conn.commit()
def delete3():
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM lakshya;")
    print(cursor.fetchall())
    x=input('Enter what information about row you have:\n1.Id\n2.Name\n3.Age\n4.Aim\nEnter choice(1/2/3/4)')
    x1=input('Enter information: ')
    if x is '1':
        cursor.execute("DELETE FROM lakshya WHERE id=?;",(x1,))
    elif x is '2':
        cursor.execute("DELETE FROM lakshya WHERE name=?;",(x1,))
    elif x is '3':
        x1=int(x1)
        cursor.execute("DELETE FROM lakshya WHERE age=?;",(x1,))
    elif x is '4':
        cursor.execute("DELETE FROM lakshya WHERE aim=?;",(x1,))
    cursor.execute("SELECT * FROM lakshya;")
    print(cursor.fetchall())
    conn.commit()
    conn.close()


def search4():
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()
    x=input('Enter what information about row you have:\n1.Id\n2.Name\n3.Age\n4.Aim\nEnter choice(1/2/3/4)')
    x1=input('Enter information: ')
    if x is '1':
        cursor.execute("SELECT * FROM lakshya WHERE id=?;",(x1,))
    elif x is '2':
        cursor.execute("SELECT * FROM lakshya WHERE name=?;",(x1,))
    elif x is '3':
        x1=int(x1)
        cursor.execute("SELECT * FROM lakshya WHERE age=?;",(x1))
    elif x is '4':
        cursor.execute("SELECT * FROM lakshya WHERE aim=?;",(x1,))
    print(cursor.fetchall())
        
def view():
    import sqlite3 as sq
    conn=sq.connect("aims.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM lakshya")
    print(cursor.fetchall())
