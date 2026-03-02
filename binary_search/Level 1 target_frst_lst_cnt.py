def solve_array(arr,target):
    start = 0 
    end = len(arr) - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            end = mid - 1 #first occurence
            #start = mid + 1 #last occurence

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return result
def solve_array_2(arr,target):
    start = 0 
    end = len(arr) - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            #end = mid - 1 #first occurence
            start = mid + 1 #last occurence

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return result

arr = [2,4,10,10,10,18,20]
target = 10

first_occurence = solve_array(arr,target)
if first_occurence == -1 :
    print(0)
else:
    last_occurence = solve_array_2(arr,target)
    print(last_occurence- first_occurence + 1)


