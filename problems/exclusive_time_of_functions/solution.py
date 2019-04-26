class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        pre = None
        for l in logs:
            fid, state, t = l.split(':')
            if not stack: stack.append((int(fid), int(t)))
            else:
                diff = int(t) - pre[0]
                if state == "end":
                    ans[int(fid)] += diff + pre[1]
                    stack.pop()
                else:
                    ans[stack[-1][0]] += diff - (1-pre[1])
                    stack.append((int(fid), int(t)))
            pre = (int(t), state == "start")
        return ans
                
        