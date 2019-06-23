class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mi, ma = None, None
        for i in range(len(count)):
            if count[i] > 0:
                mi = i
                break
        for i in range(len(count)-1, -1, -1):
            if count[i] > 0:
                ma = i
                break
        total = 0
        cnt = 0
        mode = 0
        for i, x in enumerate(count):
            if x > count[mode]:
                mode = i
            if x:
                total += i * x
                cnt += x
        mean = total / cnt
        curr = 0
        pre = -1
        for i, x in enumerate(count):
            curr += x
            if curr >= cnt // 2 + 1:
                if cnt % 2 == 1 or curr - x < cnt // 2:
                    median = i
                else:
                    median = (i + pre) / 2
                break
            if x:
                pre = i
                
        return [float(mi), float(ma), float(mean), float(median), float(mode)]
                
        