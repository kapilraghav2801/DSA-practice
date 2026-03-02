#arr = [7,10,4,3,20,15]  #[3,4,7,10,15,20]
# k = 3

# arr.sort()
# print(arr)
# print(arr[2])

def sort(arr,):
    n = len(arr)
    for i in range(n):
        for j in range(1,n):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j], arr[j-1]

    return arr

arr = [7,10,4,3,20,15]  #[3,4,7,10,15,20]
#k = 3

print(sort(arr))