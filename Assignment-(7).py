def bubble_sort():
    s = eval(input('Enter a list: '))
    for i in range(len(s)):
        for j in range(i +1, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    print('Sorted list: ',s)

def insertion_sort():
    l = eval(input('Enter a list: '))
    for i in range(1, len(l)):
        k = l[i]
        j = i-1
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            j -= 1
        else:
            l[j+1] = k
    print('sorted list:' ,l)
g = 'y'
while g == 'y':
    choice = input('Press 1 for bubble sorting. Press 2 for insertion sorting.')
    if choice == '1':
        bubble_sort()
    elif choice == '2':
        insertion_sort()
    else:
        print('Invalid Input. Try Again !')
    g = input('Do you want to continue ?')    
