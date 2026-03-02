def print_1_to_n(n):
    if n == 0:
        return
    
    print_1_to_n(n-1)

    print(n)

print_1_to_n(4)

def my_pow(x,n):
    if n == 0:
        return 1
    if n<0:
        return 1/my_pow(x,-n)
    
    smaller = my_pow(x,n-1)

    return x * smaller

print(my_pow(2,-3))

def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)

    half = my_pow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


print(my_pow(2, -3))   # 0.125
print(my_pow(2, 5))   # 32
print(my_pow(2, 0))    # 1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(6))


def fib(n):
    if n <= 1:
        return n
    
    last = fib(n-1)
    second_last = fib(n-2)
    
    return last + second_last
print(fib(6))


def fib(n, memo=None):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(6))  # 8


