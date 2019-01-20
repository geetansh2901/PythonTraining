import sqlite3 as sq
conn=sq.connect("courses.db")
cursor=conn.cursor()
#cursor.execute("CREATE  TABLE courses(number INTEGER PRIMARY KEY, name text, ects real);") 
#cursor.execute("INSERT INTO courses VALUES ('02820','Python Programming',5);")
#cursor.execute("INSERT INTO courses VALUES ('02821','Python Programming Suckes',420);")
cursor.execute("SELECT * FROM courses;")
x=cursor.fetchone()# returns one row at a time with fetchone

#print(cursor.fetchone())
#print(cursor.fetchone())
#print(cursor.fetchone())

#parameterized input
#courses=("02457","non linear signal processing",10)
#cursor.execute("INSERT INTO courses VALUES(?,?,?);",courses)

#courses=[("02454","Intro to cognitive science",5),("02451","Digital Signal Processing",10)]
#cursor.executemany("INSERT INTO courses VALUES(?,?,?);",courses)

#cursor.execute("SELECT * FROM courses;") 
#for row in cursor:print(row)

#cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")
#c=cursor.fetchall()

#c=cursor.execute("SELECT * FROM courses WHERE number=? OR name=? OR ects=?;",("2451","Intro to cognitive science",420))
#print(cursor.fetchall())

#d={'number':2454}
#cursor.execute("SELECT name FROM courses WHERE number=?;",(d['number'],))
#print(cursor.fetchall())

#cursor.execute("UPDATE courses SET name=?, ects=? WHERE number=?;",('HECK',0,2454))
#cursor.execute("SELECT * FROM courses;")
#print(cursor.fetchall())

cursor.execute("DELETE FROM courses WHERE number=?;",('2821',))
cursor.execute("SELECT * FROM courses;")
print(cursor.fetchall())
conn.commit()
conn.close()



