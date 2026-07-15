def fibbonacci(list):
    global fib
    fib =[0,1]
    for i in range(2,list):
        fib.append(fib[-1] + fib[-2])
    return fib
def multi_fibbo(list):
    fib7 = []
    for i in fib:
        i *= 7
        fib7.append(i)
    return fib7        

k = 'y'
while k == 'y':
    n = int(input('Enter the number of terms: '))
    x = fibbonacci(n)
    print('The list of',n,'terms is: ',x) 
    y = multi_fibbo(n)
    print('List after multiplying each elements with 7: ',y) 
    k = input('Do you want to continue ?')
 #print('The list of',list,'terms is: ',fib) print('List after multiplying each elements with 7: ',fib7)  
