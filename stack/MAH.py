arr = [6,2,5,4,5,1,6]

def MAH(arr):
    n = len(arr)
    stack = []
    NSL = [] 
    for i in range(n):
        while stack and arr[stack[-1]] >= arr [i]:
            stack.pop()
        if not stack:
            NSL.append(-1)
        else:
            NSL.append(stack[-1])
        stack.append(i)
    stack = []
    NSR = []
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if not stack:
            NSR.append(n)
        else:
            NSR.append(stack[-1])
        stack.append(i)
    NSR.reverse()
    
    max_area = 0
    for i in range(n):
        width = NSR[i] - NSL[i] - 1
        area = arr[i] * width
        max_area = max(max_area, area)
    return max_area