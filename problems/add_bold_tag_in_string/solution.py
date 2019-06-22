from collections import defaultdict
from bisect import bisect_left as bl
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        words = defaultdict(set)
        for w in dict:
            words[len(w)].add(w)
        ls = sorted(words.keys(), reverse=True)
        stack = [] # (i, j, bolded)
        i = j = curr = 0
        while i < len(s):
            bolded = False
            while curr <= j:
                for l in ls:
                    if s[curr:curr+l] in words[l]:
                        j = max(curr + l - 1, j)
                        bolded = True
                        break
                curr += 1
            if stack and stack[-1][-1] == bolded:
                i = stack.pop()[0]
            stack.append((i, j, bolded))
            i = j = curr
        ans = ""
        for i, j, bolded in stack:
            curr = s[i:j+1]
            ans += ("<b>{}</b>" if bolded else "{}").format(curr)
        return ans