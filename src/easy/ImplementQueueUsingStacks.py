from queue import LifoQueue


class MyQueue:

    def __init__(self):
        self.main_stack = LifoQueue()
        self.helper_stack = LifoQueue()

    def push(self, x: int) -> None:
        if self.main_stack.qsize() == 0 and self.helper_stack.qsize() > 0:
            self.move_from_helper_to_main()

        self.main_stack.put(x)

    def pop(self) -> int:
        if self.main_stack.qsize() > 0 and self.helper_stack.qsize() == 0:
            self.move_from_main_to_helper()

        return self.helper_stack.get()

    def move_from_helper_to_main(self):
        while self.helper_stack.qsize() > 0:
            self.main_stack.put(self.helper_stack.get())

    def move_from_main_to_helper(self):
        while self.main_stack.qsize() > 0:
            self.helper_stack.put(self.main_stack.get())

    def peek(self) -> int:
        if self.main_stack.qsize() > 0 and self.helper_stack.qsize() == 0:
            self.move_from_main_to_helper()

        item = self.helper_stack.get()
        self.helper_stack.put(item)

        return item

    def empty(self) -> bool:
        return self.main_stack.qsize() == 0 and self.helper_stack.qsize() == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
