import mysql.connector as m
mycon = m.connect(host="localhost", user="root",\
                  password="debjeet", database="xii")
c = mycon.cursor()

c.execute("create table studentyo(roll int,name varchar(10),marks int)")
k = 'y'
while k == 'y':
    n = int(input("Enter the Number of Data(s) to be Inserted: "))
    for i in range(n):
        roll = int(input("\nEnter Roll No.: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        c.execute(f"insert into student values({roll},'{name}',{marks})")

    print("\nInserted Data(s): ")
    c.execute("select * from student")
    for i in c.fetchall():
        print(i)

    c.execute("update student set name='Shreya' where roll = 3")
    print("\nUpdated Data(s): ")
    c.execute("select * from student")
    for i in c.fetchall():
        print(i)
    mycon.commit()
    k = input("Do you want to continue ?")

