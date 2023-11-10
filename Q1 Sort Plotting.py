import time
import numpy as np
import matplotlib.pyplot as plt

def selectionSort(alist):

   for i in range(len(alist)):
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp
       
def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    
    i = 0     
    j = 0     
    k = l     

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
    if l < r:
        m = l + (r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        
def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]     

    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def pySort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        pySort(arr, low, pi-1)
        pySort(arr, pi+1, high)
        
def bubbleSort(array1):
    max_val = max(array1)
    m = max_val + 1
    count = [0] * m

    for a in array1:
    # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array1[i] = a
            i += 1

sorts = [
    {
        "name": "Selection Sort",
        "sort": lambda arr: selectionSort(arr)
    },
    {
        "name": "Insertion Sort",
        "sort": lambda arr: insertionSort(arr)
    },
    {
        "name": "Bubble Sort",
        "sort": lambda arr: bubbleSort(arr)
    },
    {
        "name": "Merge Sort",
        "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
    },
    {
        "name": "Py Sort",
        "sort": lambda arr: pySort(arr, 0, len(arr) - 1)
    }
]

elements = np.array([i*50 for i in range(1, 10)])

plt.xlabel('Length')
plt.ylabel('Time')

for sort in sorts:
    times = list()
    start_all = time.time()
    for i in range(1, 10):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        sort["sort"](a)
        end = time.time()
        times.append(end - start)

    end_all = time.time()
    plt.plot(elements, times, label = sort["name"], linewidth=3,)

plt.grid()
plt.legend()
plt.show()
