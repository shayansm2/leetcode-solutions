# there are three ways in order to use stacks
# 1. the simplest one: lists
# 2. the standard one: queue module
# 3. the "reinvent the wheel" one: linked lists

########################################################################################################################
# 1. list stack
list_stack = []

list_stack.append('a')
list_stack.append('b')
list_stack.append('c')

print(len(list_stack))

print(list_stack.pop())
print(list_stack.pop())
print(list_stack.pop())

########################################################################################################################
# 2. queue module
from queue import LifoQueue

# Initializing a stack
py_stack = LifoQueue(maxsize=3)

# put() function to push element in the stack
py_stack.put('a')
py_stack.put('b')
py_stack.put('c')

# qsize() show the number of elements in the stack
print(py_stack.qsize())

# get() function to pop element from stack in LIFO order

print(py_stack.get(), ' poped from stack')
print(py_stack.get(), ' poped from stack')
print(py_stack.get(), ' poped from stack')

# qsize() show the number of elements in the stack
print(py_stack.qsize())


########################################################################################################################
# 3. linked lists
class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if self.is_empty():
            raise Exception('empty stack')

        self.top: StackNode
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item) -> None:
        node = StackNode(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.is_empty():
            raise Exception('empty stack')

        self.top: StackNode
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None


linked_list_stack = LinkedListStack()

linked_list_stack.push('a')
linked_list_stack.push('b')
linked_list_stack.push('c')

print(linked_list_stack.pop(), ' poped from stack')
print(linked_list_stack.peek(), 'last item in stack')
print(linked_list_stack.is_empty())
