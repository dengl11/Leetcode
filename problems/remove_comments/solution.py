from collections import deque
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        blockMode = False
        source = deque(source)
        l = source.popleft()
        pre = ""
        while l or source:
            if not l: 
                l = source.popleft()
                if pre and not blockMode:
                    ans.append(pre)
                    pre = ""
            if blockMode:
                end = l.find("*/")
                if end < 0: 
                    l = source.popleft()
                else:
                    l = pre + l[end+2:]
                    pre = ""
                    blockMode = False
            else:
                hasComment = False
                for i in range(len(l)-1):
                    if l[i:i+2] == "//":
                        pre += l[:i]
                        l = ""
                        hasComment = True
                        break
                    if l[i:i+2] == "/*":
                        pre += l[:i]
                        blockMode = True
                        l = l[i+2:]
                        hasComment = True
                        break
                if not hasComment:
                    if pre: ans.append(pre)
                    ans.append(l)
                    l = pre = ""
        if pre:ans.append(pre)
        return ans
                        
        