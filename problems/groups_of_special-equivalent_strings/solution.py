
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def hash(s):
            evens, odds = [], []
            for i in range(len(s)):
                if i % 2 == 0:
                    odds.append(s[i])
                else:
                    evens.append(s[i])
            return (len(s), "".join(sorted(odds) + sorted(evens)))
        
        hashes = set()
        for a in A:
            hashes.add(hash(a))
        return len(hashes)