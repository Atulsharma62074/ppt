l1 = [4,5,8]
l2=[14,15,19]
s1 = len(l1)
s2 = len(l2)

res = []
i, j = 0, 0

while i < s1 and j < s2:
	if l1[i] < l2[j]:
		res.append(l1[i])
		i += 1

	else:
		res.append(l2[j])
		j += 1

res = res + l1[i:] + l2[j:]
print("The combined sorted list is : " + str(res))
