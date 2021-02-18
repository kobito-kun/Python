arr = [5,4,3,2,1] #Default Array


def bubbleSort(arr):
	l = len(arr)
	for j in range(l):
		for i in range(0, l-j-1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)
bubbleSort(arr)
print(arr)