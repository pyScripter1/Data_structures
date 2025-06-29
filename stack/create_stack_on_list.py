# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
#
# Think of it like a stack of pancakes - you can only add or remove pancakes from the top.


'''
Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
'''

# Stacks can be implemented by using arrays or linked lists.
#
# Stacks can be used to implement undo mechanisms, to revert to previous states, to create algorithms for depth-first search in graphs, or for backtracking.
#
# Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.


# Use a python list as a stack

stack = [1, 2, 3, 4, 5, 6, 7]

# push
stack.append(8)
stack.append(9)
stack.append(10)
print(f"stack: {stack}")

# peek
top_element = stack[-1]
print(top_element)

# pop
popped_element = stack.pop()
print(popped_element)

# stack aftef pop
print(stack)

# isEmpty
print(not bool(stack))

# size
print(f"Size: {len(stack)}")


