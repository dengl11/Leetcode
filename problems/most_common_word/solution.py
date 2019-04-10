from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = Counter([w for w in paragraph.lower().replace(",", " ").replace(".", " ").\
                     replace("!", " ").replace("?", " ").replace("'", " ").replace(";", " ").split()])
        for w in banned:
            c[w.lower()] = 0
        return max((v, k) for (k, v) in c.items())[1]