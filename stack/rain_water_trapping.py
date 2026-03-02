arr = [4,2,0,3,2,5]

def max_left_right(arr):
    n = len(arr)
    max_left = [arr[0]]
    max_right = [arr[-1]]

    for i in range(1,n):
        max_left.append(max(max_left[-1],arr[i]))
        

    for i in range(n-2,-1,-1):
        max_right.append(max(max_right[-1],arr[i]))
    max_right.reverse()

    return max_left, max_right

water = 0
n = len(arr)
left,right = max_left_right(arr)

for i in range(n):
    water += min(left[i],right[i]) - arr[i]

print("Water Trapped: ", water)
