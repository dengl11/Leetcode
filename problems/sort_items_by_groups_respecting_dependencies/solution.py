from collections import defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        clusters = defaultdict(list)
        for i, g in enumerate(group):
            if g < 0:
                m += 1
                group[i] = m
                clusters[m].append(i)  
            else:
                clusters[g].append(i)
        
        in_cluster_after = defaultdict(lambda:defaultdict(list))
        cross_cluster_after = defaultdict(list)
        
        after = defaultdict(set)
        for i, befores in enumerate(beforeItems):
            for b in befores:
                if group[b] == group[i]:
                    in_cluster_after[group[i]][b].append(i)
                else:
                    cross_cluster_after[group[b]].append(group[i])
        
        def topological_sort(nodes : list, after : dict):
            """
            len(ans) < len(nodes) if cycle detected
            """
            ans = []
            colors = defaultdict(int)
            def dfs(i):
                if colors[i] == -1: return True
                if colors[i] == 1: return False
                colors[i] = 1
                for a in after[i]:
                    if not dfs(a): return False
                colors[i] = -1
                ans.append(i)
                return True
            starts = set(nodes)
            for arr in after.values():
                for n in arr:
                    starts.discard(n)
            for n in starts:
                if dfs(n) is False: return []
            ans.reverse()
            return ans
        
        ordered_clusters = topological_sort(list(clusters.keys()), cross_cluster_after)
        if len(ordered_clusters) < len(clusters): return []
        
        
        ans = []
        for cluster in ordered_clusters:
            ordered = topological_sort(clusters[cluster], in_cluster_after[cluster])
            if len(ordered) < len(clusters[cluster]): return []
            ans += ordered
        return ans
            
    
        
            
            