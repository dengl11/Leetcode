class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        target, r = divmod(sum(machines), n)
        if r: return -1
        toLeft = ans = 0
        for x in machines:
            toRight = x - toLeft - target
            ans = max(ans, toLeft, toRight, toLeft + toRight)
            toLeft = -toRight
        return ans