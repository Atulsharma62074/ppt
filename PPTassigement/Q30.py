def findMin(arr, N):
	ml = arr[0];
	for i in range(N) :
		if arr[i] < ml :
			ml = arr[i]

	return ml
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)
print(findMin(arr,N))
