def stockSpan(prices):
    stack = []
    span = []
    for i,price in enumerate(prices):
        while stack and stack[-1][0] <= price:
            stack.pop()

        span.append(i - stack[-1][1] if stack else i + 1)

        stack.append((price,i))

    return span

prices = [100,80,60,70,60,75,85]

print(stockSpan(prices))