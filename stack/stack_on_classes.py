'''
Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.
'''

# While Python lists can be used as stacks,
# creating a dedicated Stack class provides better encapsulation and additional functionality:

class Stack:
    def __init__(self):
        self.stack = [] # create a empty list

    def __str__(self):
        return f"[{', '.join(list(map(str, self.stack)))}]"

    def push(self, element): # push elements into stack
        self.stack.append(element)

    def peek(self): # return element at the top
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self): # remove and returns removed element from stack
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_empty(self): # check that empty stack or not
        return len(self.stack) == 0

    def size(self):
        return len(self.stack) # return size of stack

myStack = Stack() # creating stack - object of Stack

# myStack.pop() - Exception
print(myStack.peek()) # None
print(myStack) # []
print(myStack.is_empty()) # True

# pushing elements
myStack.push(3)
myStack.push(8)
myStack.push(10)
myStack.push(23)
print(myStack)

# peek
print(myStack.peek())

# pop
myStack.pop()
myStack.pop()
print(myStack)

# is_empty
print(myStack.is_empty())