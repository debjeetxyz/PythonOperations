import mysql.connector as m
mycon = m.connect(host="localhost", user="root", password="debjeet", database="assignment")
c = mycon.cursor()

c.execute("create table students(roll int,name varchar(10),percent int)")
k = 'y'
while k == 'y':
    n = int(input("Enter the Number of Data(s) to be Inserted: "))
    for i in range(n):
        roll = int(input("\nEnter Roll No.: "))
        name = input("Enter Name: ")
        percent = int(input("Enter Percent: "))
        c.execute(f"insert into students values({roll},'{name}',{percent})")

    print("\nInserted Data(s): ")
    c.execute("select * from students")
    for i in c.fetchall():
        print(i)

    c.execute("delete from students where percent < 40")
    print("\nData(s) After Deletion: ")
    c.execute("select * from students")
    for i in c.fetchall():
        print(i)
    mycon.commit()
    k = input("Do you want to continue ?")

