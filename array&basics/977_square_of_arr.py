

def square_of_sorted_arr(arr):
  result = []

  for num in arr:
    result.append(num ** 2)

  result.sort()

  return result
arr = [-4,-1,0,3,10]
print(square_of_sorted_arr(arr))    #O(nlogn)


def square_of_sorted_arr(arr):
    n = len(arr)
    left = 0
    right = n - 1
    result = []

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1

        else:
            result.append(arr[right] ** 2)
            right -= 1
    result.reverse()

    return result
arr = [-4,-1,0,3,10]

print(square_of_sorted_arr(arr))




