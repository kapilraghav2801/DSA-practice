nums = [1,3,2,4]
def NGL(nums):
    stack = []
    result = []
    for num in nums:
        while stack and stack[-1] <= num:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(num)

    return result

print(NGL(nums))