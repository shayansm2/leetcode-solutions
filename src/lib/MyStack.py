from typing import Optional


class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack(object):
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
