nums = [1,3,2,4]

def NSR(nums):
    stack = []
    result = []
    for num in reversed(nums):
        while stack and stack[-1] >= num:
            stack.pop()

        result.append(stack[-1] if stack else -1)
        stack.append(num)

    return result[::-1]

print(NSR(nums))