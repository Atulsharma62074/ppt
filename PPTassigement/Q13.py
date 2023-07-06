ini_str = "abc"

print("Initial string", ini_str)

# Finding all permutation
result = []

def permute(data, i, length):
	if i == length:
		result.append(''.join(data) )
		print("\n",result)
	else:
		for j in range(i, length):
			# swap
			data[i], data[j] = data[j], data[i]
			print(data[i],data[j])
			permute(data, i + 1, length)
			data[i], data[j] = data[j], data[i]
			print(data[i],data[j])
permute(list(ini_str), 0, len(ini_str))

# Printing result
print("Resultant permutations", str(result))
