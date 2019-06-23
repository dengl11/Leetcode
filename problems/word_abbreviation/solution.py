from collections import defaultdict
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        ans = [w if len(w) <= 3 else w[0] + str(len(w) - 2) + w[-1] for w in words ]
        groups = defaultdict(list)
        for i, w in enumerate(words):
            groups[(w[0], w[-1], len(w))].append((i, w))
        
        def abbreviate(group, s, l):
            if len(group) <= 1: return
            def trim(group, prefix):
                if prefix >= l - 2:
                    for i, w in group:
                        ans[i] = w
                elif len(group) == 1:
                    i, w = group[0]
                    if prefix >= l - 2: ans[i] =  w
                    else:
                        ans[i] = w[:prefix] + str(l - prefix - 1) + w[-1]
                else:
                    prefix += 1
                    ng = defaultdict(list)
                    for i,w in group:
                        ng[w[prefix-1]].append((i, w))
                    for g in ng.values():
                        trim(g, prefix)
            trim(group, 1)
                        
        for k, g in groups.items():
            abbreviate(g, k[0], k[-1])
            
        return ans