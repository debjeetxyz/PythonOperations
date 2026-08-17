x = int(input("Enter the number of rows: "))
r = [1]
for i in range(x):
  print(' '*(x-i-1),end = '')
	print(*(r))
	r  = [ l + e for l,e in zip([0] + r , r + [0])]
