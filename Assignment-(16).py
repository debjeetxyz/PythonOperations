def write():
    f = open("classXII.txt","w")
    n = int(input('Enter no. of students: '))
    for i in range(n):
        nme = input("\nEnter Student Name: ")
        subj = input("Enter Subject: ")
        clas =  input("Enter Class: ")
        w = (f"{nme} {subj} {clas}")
        f.write(w)
    print("Text Successfully Written. ")
    f.close()
    
def read():
    f = open("classXII.txt","r")
    r = f.read().split()
    vowels = 'aeiouAEIOU'
    v, c = [], []
    for i in r:
        if any(char in vowels for char in i):
            v.append(i)
        elif any(char not in vowels for char in i):
            c.append(i)
    print("Words with vowels: ",v,"\nWords with consonants: ",c)         

write()
read()

