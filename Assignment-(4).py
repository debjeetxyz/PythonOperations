def nat_sum():
    s = int(input('Enter the starting range: '))
    e = int(input('Enter the ending range: '))
    sum = 0
    for i in range(s, e+1):
        sum += i
    print('Summation of all the natural numbers: ',sum)
    def odd_even():
        nonlocal s,e
        sum1 = 0
        sum2 = 0
        for j in range(s,e+1):
            if j%2 == 0:
                sum1 += j
            else:
                sum2 += j
        print('Summation of odd no.s: ',sum2,'\nSummation of even no.s: ',sum1)
    odd_even()

def factorial():
    n = int(input('Enter the number: '))
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print('Factorial of',n,'is: ',fact)

k = 'y'
while k == 'y':
    choice = int(input('Press 1 for summation of natural numbers.\
\nPress 2 for factorial of a given\
number.'))
    if choice == 1:
        nat_sum()
    elif choice == 2:
        factorial()
    else:
        print('Invalid input : Try Again !!!')
    k = input('Do you want to continue ?')     
