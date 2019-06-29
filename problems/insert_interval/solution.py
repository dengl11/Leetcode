class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        i = 0
        while i < len(intervals):
            if newInterval is not None and newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                newInterval = None
                continue
            if newInterval is None or intervals[i][1] < newInterval[0]: 
                ans.append(intervals[i])
                i += 1
                continue
            end = max(intervals[i][1], newInterval[1])
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            ans.append([min(intervals[i][0], newInterval[0]), end])
            i = j
            newInterval = None
                
        if newInterval is not None:
            ans.append(newInterval)
        return ans
            
            