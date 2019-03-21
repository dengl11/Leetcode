from bisect import bisect_left
from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        idx = bisect_left(arr, (timestamp, ""))
        if idx >= len(arr) or arr[idx][0] != timestamp:
            idx -= 1
        if idx < 0: return ""
        return arr[idx][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)