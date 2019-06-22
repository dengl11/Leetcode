class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {
            "0": "0",
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
        }
        ans = ""
        for c in num[::-1]:
            if c not in pairs: return False
            ans += pairs[c]
        return ans == num
            