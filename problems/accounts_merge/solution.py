from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(list)
        for e in accounts:
            emails[e[0]].append(e[1:])
        ans = []
        for name, groups in emails.items():
            belongTo = {i:i for i in range(len(groups))}
            def query(i):
                if i == belongTo[i]: return i
                belongTo[i] = query(belongTo[i])
                return belongTo[i]
                    
            merged = []
            for i, emails in enumerate(groups):
                merged += [(e, i) for e in emails]
            merged.sort()
            pre = merged[0][0]
            for i in range(1, len(merged)):
                if merged[i][0] != pre:
                    pre = merged[i][0]
                else:
                    belongTo[query(merged[i][1])] = query(belongTo[merged[i-1][1]])
            for i in range(len(groups)):
                root = query(i)
                if root == i: continue
                groups[root] += groups[i]
                groups[i] = None
            for g in groups:
                if g is None: continue
                ans.append([name] + sorted(set(g)))
        return ans
                
                    
                
                
        