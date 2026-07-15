def startP(str):
    listp = []
    for i in str.split():
        if i.startswith('P') or i.startswith('p'):
            listp.append(i)
    print('Words starting with \'p\': ',listp)            
        
def endsi(str):
    listi = []
    for i in str.split():
        if i.endswith('i'):
            listi.append(i)
    print('Words starting with \'i\': ',listi)            
        
def length(str):
    lis = []
    for i in str.split():
        lis.append((len(i)))
    print('Length of each and every word: ',tuple(lis))
    
k = 'y'
while k == 'y':
    string = input('Enter a string: ')
    startP(string)
    endsi(string)
    length(string)
    k = input('Do you want to continue ?')








































































































































































