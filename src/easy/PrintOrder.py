from threading import Semaphore

class Foo:
    def __init__(self):
        self.first_lock = Semaphore(1)
        self.second_lock = Semaphore(0)
        self.third_lock = Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.first_lock.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


import concurrent.futures

def getPrinter(whatToPrint: str):
    def printer():
        print(whatToPrint)
    return printer

with concurrent.futures.ThreadPoolExecutor() as executor:
    foo = Foo()
    executor.submit(foo.third, getPrinter("third"))
    executor.submit(foo.second, getPrinter("second"))
    executor.submit(foo.first, getPrinter("first"))