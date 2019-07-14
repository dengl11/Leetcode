from threading import Semaphore
class Foo:
    def __init__(self):
        self.first_done = Semaphore(0)
        self.second_done = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_done:
            printSecond()
            self.second_done.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_done:
            printThird()

        