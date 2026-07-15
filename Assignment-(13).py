import mysql.connector as m
mycon = m.connect(host="localhost", user="root", password="debjeet", database="fr")
c = mycon.cursor()

c.execute("create table employee(eid int,name varchar(10),salary int,city varchar(12))")
k = 'y'
while k == 'y':
    n = int(input("Enter the Number of Data(s) to be Inserted: "))
    for i in range(n):
        eid = int(input("\nEnter EID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        city = input("Enter City: ")
        c.execute(f"insert into employee values({eid},'{name}',{salary},'{city}')")

    c.execute("select * from employee")
    data = c.fetchall()
    count = c.rowcount
    print("\nThe Total No. of Rows: ",count)
    print("\nInserted Data(s): ")
    for i in data:
        print(i)

    print("\nEmployees whose salary is greater then 35000:")
    c.execute("select * from employee where salary > 35000")
    for i in c.fetchall():
        print(i)
    mycon.commit()
    k = input("Do you want to continue ?")


