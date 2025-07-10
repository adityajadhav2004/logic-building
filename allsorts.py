# bubble sort 
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr1 = [3,4,4,4,4,33,3]
bubblesort(arr1)
print(arr1)

