from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        maxL = max(len(w) for w in words)
        G = defaultdict(set)
        allNodes = set(c for w in words for c in w )
        for i in range(maxL):
            for j in range(len(words)-1):
                if len(words[j]) <= i or len(words[j+1]) <= i:
                    continue
                if words[j][:i] == words[j+1][:i]:
                    if words[j][i] != words[j+1][i]:
                        # print(words[j][i], words[j+1][i])
                        G[words[j][i]].add(words[j+1][i])
        # print(allNodes)
        # print(G)
        def topological(G):
            colors = defaultdict(int)
            L = deque()
            self.cycle = False
            def dfs(node):
                if colors[node] == 1: 
                    self.cycle = True
                    return
                if colors[node] == -1: return 1
                colors[node] = 1
                for n in G[node]:
                    dfs(n)
                    if self.cycle: return
                colors[node] = -1
                L.appendleft(node)
                
            for n in allNodes:
                curr = dfs(n)
            if self.cycle: return []
            return L
        ans = topological(G)
        if ans is None: return ""
        return "".join(ans)
                    