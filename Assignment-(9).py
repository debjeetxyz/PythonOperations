def palin(str):
    pl = []
    for i in str.split():
        if i == i[ : :-1]:
            pl.append(i)
    print('Words which are palindrome: ',pl)

def reverse(str):
    print('Reverse of a given string: ',str[ : : -1])

string = input('Enter a string: ')
k = 'y'
while k == 'y':
    palin(string)
     reverse(string)
    k = input('Do you want to continue ?')
