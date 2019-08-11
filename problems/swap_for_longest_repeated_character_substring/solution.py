from collections import defaultdict
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        segs = defaultdict(list)
        for i, c in enumerate(text):
            if not segs[c] or i > segs[c][-1][1] + 1: segs[c].append([i, i])
            else:
                segs[c][-1][1] += 1
        ans = 1
        for c, parts in segs.items():
            curr = max(parts[i][1] - parts[i][0] + 1 for i in range(len(parts)))
            ans = max(ans, curr)
            if len(parts) > 1: 
                ans = max(ans, curr + 1)
                for i in range(len(parts) - 1):
                    if parts[i][1] == parts[i+1][0] - 2:
                        if len(parts) > 2:
                            ans = max(ans, parts[i + 1][1] - parts[i][0] + 1)
                        else:
                            ans = max(ans, parts[i + 1][1] - parts[i + 1][0] + parts[i][1] - parts[i][0] + 2)
                    elif len(parts) > 1:
                        ans = max(ans, parts[i][1] - parts[i][0] + 2)
                        
        return ans
        
        # ans = 1
        # text = list(text)
        # for i in range(len(text)):
        #     for j in range(len(text)):
        #         if text[i] == text[j]: continue
        #         text[i], text[j] = text[j], text[i]
        #         left = j
        #         while left > 0 and text[left - 1] == text[j]: left -= 1
        #         right = j
        #         while right + 1 < len(text) and text[right + 1] == text[j]: right += 1
        #         ans = max(ans, right - left + 1)
        #         text[i], text[j] = text[j], text[i]
        # return ans