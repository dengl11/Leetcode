from bisect import insort
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.L = []
        

    def seat(self) -> int:
        ans = 0
        if self.L: 
            dist = self.L[0]
            for i, j in zip(self.L, self.L[1:]):
                if (j-i) // 2 > dist:
                    dist = (j-i)//2
                    ans = (j+i)//2
            if self.N-1-self.L[-1]> dist:
                ans = self.N-1
        insort(self.L, ans)
        return ans
            
        
    def leave(self, p: int) -> None:
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)