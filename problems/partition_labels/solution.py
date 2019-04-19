class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        latest = [0]*26
        for pos, c in enumerate(S):
            i = ord(c) - ord('a')
            latest[i] = max(latest[i], pos)
        ans = []
        pre = 0
        need = latest[ord(S[0]) - ord('a')]
        for pos, c in enumerate(S): 
            i = ord(c)-ord('a')
            if pos > need:
                need = latest[i]
                ans.append(pos-pre)
                pre = pos
            else:
                need = max(need, latest[i])
        ans.append(need + 1 - pre)
        return ans
                
            