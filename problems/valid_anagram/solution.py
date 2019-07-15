class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        encode = lambda s: "".join(sorted(s))
        return encode(s) == encode(t)
        