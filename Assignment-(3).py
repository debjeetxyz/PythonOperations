def create():
    global l1,l2,n
    n = int(input('Enter the no. of elements: '))
    l1,l2 = [],[]
    for i in range(n):
        a = int(input('Enter element for first list: '))
        b = int(input('Enter element for second list: '))
        l1.append(a)
        l2.append(b)
    print('List - 1 : ',l1,'\nList - 2 : ',l2)
    
def add_list():
    l3 = []
    for j in range(n):
        c = l1[j] + l2[j]
        l3.append(c)
    print('Summation of the above two list is : ',l3)
    
def multi_list():
    l4 = []
    for j in range(n):
        c = l1[j] * l2[j]
        l4.append(c)
    print('Multiplication of the above two list is : ',l4)
    
k = 'y'
while k == 'y':
    create()
    add_list()
    multi_list()
    k = input('Do you want to continue ?')
