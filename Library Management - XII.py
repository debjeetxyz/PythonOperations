import mysql.connector as a
con = a.connect(host = 'localhost',user = 'root',password = 'debjeet',database = 'library')
c = con.cursor()

c.execute("create table if not exists books(bname varchar(50), author varchar(50), bcode varchar(4), subject varchar(50), primary key(bcode))")
c.execute("create table if not exists issue(name varchar(20), regno int, bcode varchar(4) references books(bcode), issue_date date default(curdate()),primary key(issue_date))")
c.execute("create table if not exists re_turn(name varchar(20), regno int, bcode varchar(4) references books(bcode), return_date date default(curdate()), primary key(return_date))")
c.execute("create table if not exists customer(cust_id int, joining_date date default(curdate()), bcode varchar(4) references books(bcode), issue_date date default(curdate()) references issue(issue_date), return_date date default(curdate()) references re_turn(return_date), unique(cust_id))")

def cust():
    ci = int(input("Enter Customer ID: "))
    jd = input("Enter joining date: ")
    bc = input("Enter Book Code: ")
    ie = input("Enter Issue Date: ")
    re = input("Enter Return Date: ")
    data = (ci, jd, bc, ie, re)
    sql = 'INSERT INTO CUSTOMER VALUES(%s,%s,%s,%s,%s);'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("\n\nCustomer Successfully Registered.........\n\n")
    wait = input("\nPress Enter to Continue.....\n\n\n\n")
    main()
    
def cust_details():
    a = "SELECT * FROM CUSTOMER;"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    if myresult:
        for i in myresult:
            print("Customer ID: ",i[0])
            print("Joining Date: ",i[1])
            print("Book Code: ",i[2])
            print("Issue Date:",i[3])
            print("Return Date:",i[4])
            print('\n')
    else:
        print("\n\nNo customers here......")
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    report()
    
def cust_search():
    bcode = input("Enter Book Code: ")
    query = "SELECT * FROM CUSTOMER WHERE bcode = %s"
    c = con.cursor()
    c.execute(query, (bcode,))
    result = c.fetchall()
    if result:
        print(f"\n\nCustomer having book of {bcode} no.:\n ")
        for i in result:
            print("Customer ID: ",i[0])
            print("Joining Date: ",i[1])
            print("Book Code: ",i[2])
            print("Issue Date:",i[3])
            print("Return Date:",i[4])
            print('\n')
    else:
        print(f"\n\nNo Customer has taken the book having book code: {bcode}.")
    wait = input("\nPress Enter to Continue.....\n\n\n\n")
    main()    
    
def addbook():
    bn = input("\nEnter Book Name: ")
    ba = input("Enter Author's Name: ")
    cn = input("Enter Book Code: ")
    s = input("Enter Genre: ")
    data = (bn, ba, cn, s)
    sql = 'INSERT INTO BOOKS VALUES(%s,%s,%s,%s);'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("\n\nBook Added Successfully..........\n\n")
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    main()
   
def issueb():
    n = input("\nEnter Customer Name: ")
    r = int(input("Enter Reg No.:"))
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    a = "INSERT INTO ISSUE VALUES(%s,%s,%s,%s);"
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print("\n\n\n\nBook Issued Successfully to: ",n)
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    main()

def returnb():
    n = input("Enter Customer Name: ")
    r = int(input("Enter Reg No.:"))
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    a = "INSERT INTO RE_TURN VALUES(%s,%s,%s,%s);"
    data =(n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    print("\n\nBook Returned By: ",n)
    con.commit()
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    main()

def dbook():
    ac=input("Enter Book Code: ")
    a="DELETE FROM BOOKS WHERE BCODE = %s;"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("\n\nBook Deleted Successfully")
    wait = input('\nPress Enter to continue ..... \n\n\n\n')
    main()

def dispbook():
    a = "SELECT * FROM BOOKS;"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    if myresult:
        for i in myresult:
            print("Book Name: ",i[0])
            print("Author: ",i[1])
            print("Book Code: ",i[2])
            print("Genre:",i[3])
            print('\n')
    else:
        print("\n\nNo books to show......")
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    main()

def report_issued_books():
    a = "SELECT * FROM ISSUE;"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    if myresult:
        for i in myresult:
            print('\nCustomer Name: ',i[0])
            print('Reg. No: ',i[1])
            print('Book Code: ',i[2])
            print('Issue Date: ',i[3])
    else:
        print("/n/nNo books issued.")
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    report()

def report_return_books():
    a="SELECT * FROM RE_TURN;"
    c=con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    if myresult:
        for i in myresult:
            print('\nCustomer Name: ',i[0])
            print('Reg. No: ',i[1])
            print('Book Code: ',i[2])
            print('Return Date: ',i[3])
    else:
        print("/n/nNo books returned.")
    wait = input('\nPress Enter to continue.....\n\n\n\n')
    report()

def search_books():
    cursor = con.cursor()
    print("Search Books")
    print("1. Search by Book Name")
    print("2. Search by Author")
    print("3. Search by Genre")
    print("4. Search by Book Code")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter Book Name: ")
        query = "SELECT * FROM books WHERE bname LIKE %s"
        cursor.execute(query, (f"%{title}%",))
    elif choice == '2':
        author = input("Enter Author: ")
        query = "SELECT * FROM books WHERE author LIKE %s"
        cursor.execute(query, (f"%{author}%",))
    elif choice == '3':
        subject = input("Enter Genre: ")
        query = "SELECT * FROM books WHERE subject LIKE %s"
        cursor.execute(query, (f"%{subject}%",))
    elif choice == '4':
        bcode = input("Enter Book Code: ")
        query = "SELECT * FROM books WHERE bcode = %s"
        cursor.execute(query, (bcode,))
    else:
        print("Invalid choice. Please try again.")
            
    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"\nBook Name: {book[0]}\nAuthor: {book[1]}\nBook Code: {book[2]}\nGenre: {book[3]}\nAvailable In Cart...")
    else:
        print("\nNo books found matching your search criteria.")
    wait = input('\nPress Enter to Continue......\n\n\n\n')
    main()

def report():
    print("""

                 R E P O R T  M E N U :-
                ----------------------------

           1. ISSUED BOOKS
           2. RETURNED BOOKS
           3. CUSTOMER DETAILS
           4. BACK TO FUNCNALITIES
           \n\n

           """)
    k = input("Enter Task No.: ")
    print('\n')
    if (k == '1'):
        report_issued_books()
    elif (k == '2'):
        report_return_books()
    elif (k == '3'):
        cust_details()
    elif (k == '4'):
        main()
    else:
        print("\nPlease Try Again.......\n\n\n")
            
def main():
    print("""
                                L I B R A R Y   M A N A G E M E N T   S Y S T E M
                                ------------------------------------------------------------


                F U N C T I O N A L I T I E S :-
               ------------------------------------
           
        1. ADD BOOK
        2. ISSUE OF BOOK
        3. RETURN OF BOOK
        4. DELETE BOOK
        5. ADD CUSTOMER
        6. SEARCH CUSTOMER
        7. SEARCH BOOKS
        8. FETCH BOOKS
        9. REPORT MENU
      10. EXIT 
         """)

    choice = input("Enter Task No. : ")
    print('\n\n')
    if(choice == '1'):
        addbook()
    elif(choice == '2'):
        issueb()
    elif(choice == '3'):
        returnb()
    elif(choice == '4'):
        dbook()
    elif(choice == '5'):
        cust()
    elif(choice == '6'):
        cust_search()
    elif(choice == '7'):
        search_books()
    elif(choice == '8'):
        dispbook()
    elif(choice == '9'):
        report()
    elif (choice == '10'):
        print("\n\nT H A N K   Y O U !!!\nV I S I T   U S   A G A I N !!!\n\n\n")
    else:
        print("\nPlease Try Again.......\n\n\n")
        main()

def passwd():
    ps = input("\n\n\nEnter Password: ")
    if ps == 'python1991':
        print('\nConnection Successful.....\n\n\n\t\t\t       W E L C O M E   \n\n\t\t\t\tT O')
        main()
    else:
        print('Wrong Password.\nEnter the correct password to get access.')
        passwd()
passwd()
