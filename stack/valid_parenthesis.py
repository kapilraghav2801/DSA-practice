def valid_parenthesis(s):
    stack = []
    #pairs = {'(':')','{':'}','[':']'}
    pairs = {')':'(', ']':'[', '}':'{'}


    for ch in s:
        if ch in '({[':
            stack.append(ch)

        else:
            if not stack:
                return False
            if stack and stack[-1] != pairs[ch]:
                return False
            stack.pop()  
            # if not stack:
            #     return False
            # if ch == ')' and stack[-1] != '(' :
            #     return False
            # if ch == ']' and stack[-1] != '[' :
            #     return False
            # if ch == '}' and stack[-1] != '{' :
            #     return False
    return not stack
print(valid_parenthesis('()'))
print(valid_parenthesis('()[]{}'))
print(valid_parenthesis('(]'))
print(valid_parenthesis('([)]'))
print(valid_parenthesis('{[]}'))
