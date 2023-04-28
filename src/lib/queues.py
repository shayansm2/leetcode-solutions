# there are three ways in order to use queues
# 1. the simplest one: lists
# 2. the standard one: queue module
# 3. the "reinvent the wheel" one: linked lists

########################################################################################################################
# 1. list queue

list_queue = []

list_queue.append(10)
list_queue.append(-21)
list_queue.append(450)

print(list_queue.pop(0))
print(list_queue.pop(0))
print(list_queue.pop(0))

########################################################################################################################
# 2. queue module
import queue

myQueue = queue.Queue(maxsize=3)

myQueue.put(10)
myQueue.put(-21)
myQueue.put(450)

print(myQueue.get())
print(myQueue.get())
print(myQueue.get())


########################################################################################################################
# 3. linked lists

class QueueNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        node = QueueNode(item)

        if self.last is not None:
            self.last: QueueNode
            self.last.next = node

        self.last = node

        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            raise Exception('empty queue')

        self.first: QueueNode
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            raise Exception('empty queue')

        self.first: QueueNode
        return self.first.data

    def is_empty(self) -> bool:
        return self.first is None


linked_list_queue = LinkedListQueue()
linked_list_queue.add(10)
linked_list_queue.add(-21)
linked_list_queue.add(450)

print(linked_list_queue.remove())
print(linked_list_queue.remove())
print(linked_list_queue.remove())
