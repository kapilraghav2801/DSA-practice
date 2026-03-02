def solve_array(arr,target):
    start = 0 
    end = len(arr) - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] <= target:
            start = mid + 1
            #end = mid - 1 #first occurence
            #start = mid + 1 #last occurence

        # elif arr[mid] < target:
        #     #result = arr[mid] for floor
        #     start = mid + 1

        else:
            result = arr[mid] #for ceiling 
            end = mid - 1

    return result

# arr = [2, 5, 8, 12, 16]
# target = 10
# arr = ["c","f","j"].    #LeetCode 744 (Paraphrased): smallest letter in the list that is strictly greater than target
# target = "a"
# print(solve_array(arr,target))

arr = [1,2,3,4,5]
k = 3, target = 3