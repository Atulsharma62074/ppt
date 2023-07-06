def power(n, P):
	if P == 0:
		return 1
	return n*power(n, P-1)
print(power(6,3))
