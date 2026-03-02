matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
def max_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    heights = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0

        print(heights)

def MAH(heights):
        n = len(heights)
        stack = []
        NSL = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            NSL.append(stack[-1] if stack else -1)
            stack.append(i)

        stack = []
        NSR = []

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            NSR.append(stack[-1] if stack else n)
            stack.append(i)

        NSR.reverse()

        max_area = 0
        for i in range(n):
            width = NSR[i] - NSL[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area

