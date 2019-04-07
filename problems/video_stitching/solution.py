class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key = lambda x: (x[0], -x[1]))
        if clips[0][0] > 0: return -1
        ans = 1
        endTime = clips[0][1]
        i = 1
        while i < len(clips):
            if endTime >= T: return ans
            ans += 1
            newEnd = endTime
            while i < len(clips) and clips[i][0] <= endTime:
                newEnd = max(newEnd, clips[i][1])
                i += 1
            if newEnd == endTime: return -1
            endTime = newEnd
            i += 1
        return ans if endTime >= T else -1
                
            