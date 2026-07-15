def dcreate():
    d = {}
    for i in range(12):
        a = input('Enter month: ')
        b = int(input('Number of days: '))
        d[a] = b
    print('The required dictionary is : ',d)
    l = []
    for k in d:
        if d[k] == 31:
            l.append(k)
    print('Months with 31 days:  ',l)
    ls = []
    for t in d.items():
        ls.append(t)
    for q in range(len(ls)):
        for p in range(q+1, len(ls)):
            if ls[q][1] > ls[p][1]:
                ls[q],ls[p] = ls[p],ls[q]
    sl = []                
    for g,h in ls:
        sl.append((g,h))
    print('The key-value pairs sorted by \
 the number of days: ',sl)   
dcreate()    
 
  
