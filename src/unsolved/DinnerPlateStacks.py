from queue import LifoQueue
from typing import Optional


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.index_pop = None
        self.index_push = None

    def push(self, val: int) -> None:
        stack = self._get_push_stack()

        if stack is not None:
            stack.put(val)
            return

        new_stack = LifoQueue(self.capacity)
        new_stack.put(val)
        self.stacks.append(new_stack)
        self.index_push = len(self.stacks) - 1
        self.index_pop = len(self.stacks) - 1

    def _get_push_stack(self) -> Optional[LifoQueue]:
        if self.index_push is not None:
            stack: LifoQueue = self.stacks[self.index_push]
            if stack.qsize() < self.capacity:
                return stack

        for index, stack in enumerate(self.stacks):
            stack: LifoQueue
            if stack.qsize() == self.capacity:
                continue

            self.index_push = index
            return stack
        return None

    def pop(self) -> int:
        stack = self._get_pop_stack()

        if stack is None:
            return -1

        return stack.get()

    def _get_pop_stack(self) -> Optional[LifoQueue]:
        if self.index_pop is not None:
            stack: LifoQueue = self.stacks[self.index_pop]
            if stack.qsize() > 0:
                return stack

        for index, stack in enumerate(self.stacks[::-1]):
            stack: LifoQueue
            if stack.qsize() == 0:
                continue

            self.index_push = min(self.index_push, index)
            self.index_pop = index
            return stack
        return None

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1

        stack: LifoQueue = self.stacks[index]

        if stack.qsize() == 0:
            return -1

        self.index_push = min(self.index_push, index)
        return stack.get()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

d = DinnerPlates(2)  # Initialize with capacity = 2
d.push(1)
d.push(2)
d.push(3)
d.push(4)
d.push(5)  # The stacks are now:  2  4
print(d.popAtStack(0))  # Returns 2.  The stacks are now:     4
d.push(20)  # The stacks are now: 20  4
d.push(21)  # The stacks are now: 20  4 21
print(d.popAtStack(0))  # Returns 20.  The stacks are now:     4 21
print(d.popAtStack(2))  # Returns 21.  The stacks are now:     4
print(d.pop())  # Returns 5.  The stacks are now:      4
print(d.pop())  # Returns 4.  The stacks are now:   1  3
print(d.pop())  # Returns 3.  The stacks are now:   1
print(d.pop())  # Returns 1.  There are no stacks.
print(d.pop())  # Returns - 1.  There are still no stacks.
#
