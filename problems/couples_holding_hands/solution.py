class DUS:
    def __init__(self, n):  # disjoint union set 模板，请参考花花酱视频
        self.parent = [i for i in range(n)]
        self.counts = 0
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:  # 优化：记录多少次merge操作。 如果不记录counts的话，需要额外的O(N)复杂度来计算
            self.counts += 1
        self.parent[px] = py
        
        
class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)//2
        dus = DUS(n)
        
        for i in range(n):
            x = row[2*i] // 2
            y = row[2*i+1] // 2
            
            if x!=y:
                dus.merge(x, y)
        
        return dus.counts
