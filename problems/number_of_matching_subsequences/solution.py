from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for w in words:
            it = iter(w)
            dic[next(it)].append(it)
        for c in S:
            for it in dic.pop(c, []):
                dic[next(it, "")].append(it)
        return len(dic[""])
            
        