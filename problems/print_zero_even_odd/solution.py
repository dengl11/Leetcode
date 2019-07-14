from threading import Condition
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.state = 0
        self.cv = Condition()
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.cv:
                self.cv.wait_for(lambda: self.state <= 0)
                printNumber(0)
                self.state = abs(self.state) if self.state != 0 else 1
                self.cv.notify_all()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(2, self.n+1, 2):
            with self.cv:
                self.cv.wait_for(lambda: self.state > 0 and self.state % 2 == 0)
                printNumber(self.state)
                self.state = -(self.state + 1)
                self.cv.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n+1, 2):
            with self.cv:
                self.cv.wait_for(lambda:self.state > 0 and self.state % 2 == 1)
                printNumber(self.state)
                self.state = -(self.state + 1)
                self.cv.notify_all()
