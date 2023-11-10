import math
import random

arr = []
print ("20 random numbers fron 1 - 100: ")
for i in range(0, 20):
    n = random.randint(1,100)
    n = n ^ 10
    arr.append(n)
    arr.sort()
print(arr)

def min(arr):
	arr_size = len(arr)
	first = second = math.inf
	for i in range(0, arr_size):
		# update both first and second if element is less than first
		if arr[i] < first:
			second = first
			first = arr[i]
		# update second if element is between first and second 
		elif (arr[i] < second and arr[i] != first):
			second = arr[i]
            
	if (second == math.inf):
		print ("No second minimum value.")
	else:
		print ('The two minimum values are', first,'and', second, ".")
min(arr)


