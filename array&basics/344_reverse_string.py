s = ["h","e","l","l","o"]

def reverse_string(s):
    #return s[::-1]
    result = []
    for ch in s:
        result.insert(0,ch)
    return result


print(reverse_string(s))


def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

s = ["h","e","l","l","o"]
print(reverse_string(s))