def insert_at_bottom(stack, value):
    # Base case: empty stack
    if len(stack) == 0:
        stack.append(value)
        return

    # Remove top element
    temp = stack.pop()

    # Insert into smaller structure
    insert_at_bottom(stack, value)

    # Put the removed element back
    stack.append(temp)


def reverse(stack):
    # Base case
    if len(stack) == 0:
        return

    # Remove the top element
    temp = stack.pop()

    # Reverse the remaining stack
    reverse(stack)

    # Insert the popped element at bottom
    insert_at_bottom(stack, temp)
