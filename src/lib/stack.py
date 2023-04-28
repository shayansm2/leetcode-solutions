# stack implementation using queue module

from queue import LifoQueue

from src.lib.MyStack import MyStack

# Initializing a stack
pyStack = LifoQueue(maxsize=3)

# put() function to push element in the stack
pyStack.put('a')
pyStack.put('b')
pyStack.put('c')

# qsize() show the number of elements in the stack
print(pyStack.qsize())

# get() fucntion to pop element from stack in LIFO order

print(pyStack.get(), ' poped from stack')
print(pyStack.get(), ' poped from stack')
print(pyStack.get(), ' poped from stack')

# qsize() show the number of elements in the stack
print(pyStack.qsize())

myStack = MyStack()

myStack.push('a')
myStack.push('b')
print(myStack.pop(), ' poped from stack')
print(myStack.peek(), 'last item in stack')
print(myStack.is_empty())
