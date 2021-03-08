import random

array = []
amount = 10

for i in range(amount):
	array.append(random.randint(1, 100))

def partition(A, lo, hi):
	i = lo
	pivot = A[hi]
	for j in range(lo, hi):
		if A[j] < pivot:
			A[i], A[j] = A[j], A[i]
			i += 1
	A[i], A[hi] = A[hi], A[i]
	return i

def quicksort(A, lo, hi):
	if lo < hi:
		p = partition(A, lo, hi)
		quicksort(A, lo, p-1)
		quicksort(A, p+1 , hi)
	return A

a = quicksort(array, 0, len(array)-1)
print(a)