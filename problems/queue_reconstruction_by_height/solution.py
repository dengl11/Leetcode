class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda p: (p[0], -p[1]))
        ans = [None] * len(people)
        for h, p in people:
            todo = p
            for j, v in enumerate(ans):
                if v is not None: 
                    continue
                else:
                    if todo: todo -= 1
                    else: 
                        ans[j] = [h, p]
                        break
        return ans
            