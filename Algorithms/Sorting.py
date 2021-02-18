arr = [3,6,1,4,6,8,2,10] # Default for testing.

def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2

		left = arr[:mid]
		right = arr[mid:]

#		print(f"{left} {right}")

		mergeSort(left)
		mergeSort(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i += 1
				#print(f"LEFT {i} {arr[k]}\n")
			else:
				arr[k] = right[j]
				#print(f"RIGHT {i} {arr[k]}")
				j += 1
			k += 1
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1

mergeSort(arr)
for i in range(len(arr)):
	print(arr[i], end=" ")
