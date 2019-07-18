class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        valid = [False] * (len(s) + 1)
        valid[-1] = True
        for i in range(len(s) - 1, -1, -1):
            stop = False
            for j in range(i + 1, len(s) + 1):
                if stop: break
                if s[i:j] in words and valid[j]:
                    valid[i] = True
                    stop = True
                    
        return valid[0]
                
        
        
        