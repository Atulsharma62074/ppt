def co(lst, x):
	c = 0
	for ele in lst:
		if (ele == x):
			c = c + 1
	return c
    
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(co(lst,x))
