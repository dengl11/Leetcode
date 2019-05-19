from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        counts = [0]*N
        dist = [0]*N
        nbrs = defaultdict(list)
        for i, j in edges:
            nbrs[i].append(j)
            nbrs[j].append(i)
        def collect(i, visited):
            visited.add(i)
            for j in nbrs[i]: 
                if j not in visited:
                    collect(j, visited)
            all_counts = sum([counts[j] for j in nbrs[i]])
            counts[i] = all_counts + 1
            dist[i] = sum([dist[j] for j in nbrs[i]]) + all_counts
            
        collect(0, set())
        def summarize(i, visited):
            visited.add(i)
            for j in nbrs[i]:
                if j in visited: continue
                dist[j] = dist[i] - counts[j] + N-counts[j]
                summarize(j, visited)
                
        summarize(0, set())
        return dist