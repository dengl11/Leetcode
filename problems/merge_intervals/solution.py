class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals: return []
        ans = []
        pre = intervals[0]
        for s, e in intervals[1:]:
            if s > pre[1]:
                ans.append(pre)
                pre = [s, e]
            else:
                pre[1] = max(pre[1], e)
        ans.append(pre)
        return ans
        