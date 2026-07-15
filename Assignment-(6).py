def cases(str):
    uc, lc = 0, 0
    for i in str:
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
    print('Number of  upper cases: ',uc,'\nNumber of lower cases: ',lc)

def vc():
    global string
    string = input('Enter a string: ')
    v, c = 0, 0
    cv = "aeiouAEIOU"
    for i in string:
        if i.isalpha():
            if i in cv:
                v += 1
            else:
                c += 1
    print('Number of  vowels: ',v,'\nNumber of consonanants: ',c)
    
def sym(str):
    sy, sp = 0, 0
    for a in str:
        if a.isalnum() != True and a != ' ':
            sy += 1
        elif a.isspace():
            sp += 1
    print('Number of symbols: ',sy,'\nNumber of spaces: ',sp)
        
def char(str):
    d, a = 0, 0
    ln = len(str)
    for i in str:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            d += 1
    print('Number of characters: ',ln,'\nNumber of digits: ',d,'\n\
Number of alphbets: ',a)            

k = 'y'
while k == 'y':    
    vc()
    cases(string)
    sym(string)
    char(string)
    k = input("Do you want to continue ?")

    










