from bisect import bisect_left as bl, bisect_right as br

class RangeModule:

    def __init__(self):
        self.data = []
        

    def addRange(self, left: int, right: int) -> None:
        i, j = bl(self.data, left), br(self.data, right)
        self.data[i:j] = [left]*(i%2==0) + [right]*(j%2 == 0)
            
        

    def queryRange(self, left: int, right: int) -> bool:
        i, j = br(self.data, left), bl(self.data, right)
        return i == j and i % 2 == 1
        

    def removeRange(self, left: int, right: int) -> None:
        i, j = bl(self.data, left), br(self.data, right)
        self.data[i:j] = [left]*(i%2==1) + [right]*(j%2 == 1)
        
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)