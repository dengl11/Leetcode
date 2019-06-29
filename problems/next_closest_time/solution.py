class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set(int(c) for c in time if c != ":")
        minutes = 60 * int(time[:2]) + int(time[-2:]) + 1
        while 1:
            minutes = minutes % (24 * 60)
            h, m = divmod(minutes, 60)
            t = "{:02}:{:02}".format(h, m)
            if all(int(c) in digits for c in t if c != ":"):
                return t
            minutes += 1
        
        