class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = [0] * 26
        for i, ch in enumerate(order):
            pos[ord(ch) - ord('a')] = i
        for i in range(1, len(words)):
            pre = words[i - 1]
            curr = words[i]
            
            for j in range(max(len(pre), len(curr))):
                if j >= len(pre): break
                if j >= len(curr): return False
                if pre[j] != curr[j]:
                    if pos[ord(pre[j]) - ord('a')] > pos[ord(curr[j]) - ord('a')]:
                        return False
                    break
                    
            
        return True