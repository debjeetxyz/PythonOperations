def prime():
    s = int(input("Starting Range: "))
    e = int(input("ending Range: "))
    pri = []
    for i in range(s,e+1):
       if i > 1:
           for n in range(2,i):
               if i % n == 0:
                   break
           else:
               pri.append(i)
    print('Prime numbers within',s,'and',e,'is: ',pri)           
               
def armstrong():
    a = int(input("Starting Range: "))
    b = int(input("ending Range: "))
    arms = []
    for i in range(a,b+1):
        s = 0
        t = i
        f = len(str(i))
        while t > 0:
            d = t % 10
            s += d**f
            t //= 10
        if s == i:
            arms.append(i)
    if arms:
        print('Armstrong numbers within',a,'and',b,'is:',arms)
    else:
        print("No armstrong numbers.")
        
k = 'y'
while k == 'y':
    choice = int(input('Press 1 for printing prime numbers within a range\nPress 2 for printing armstrong numbers within a range.\n'))
    if choice == 1:
        prime()
    elif choice == 2:
        armstrong()
    else:
        print('Try Again!!! Enter a valid choice.')
    k = input('\nDo you want to continue ?')
