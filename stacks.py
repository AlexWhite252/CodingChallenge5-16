# Lists in Python can be treated as stacks, so we intialize an empty list
stack = []

# Append can be used to push onto stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

# Pop can be used to pop off of stack
stack.pop()
print(stack)

# Since the stack is a List you can use the min function, which is O(1) complexity

print(min(stack))