import mysql.connector as m
mycon = m.connect(host="localhost", user="root", password="debjeet", database="fr")
c = mycon.cursor()
k = 'y'
while k == 'y':
    print("\nEmployees whose salary is less than 50000:")
    c.execute("select * from employee where salary < 50000")
    dat = c.fetchmany(2)
    for i in dat:
        print(i)
    k = input("Do you want to continue ?")





