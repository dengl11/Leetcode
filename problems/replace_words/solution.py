from collections import defaultdict
from functools import reduce
class Solution:
    def replaceWords(self, words: List[str], sentence: str) -> str:
        T = lambda: defaultdict(T)
        trie = T()
        for w in words:
            reduce(dict.__getitem__, w, trie)['#'] = True
        words = []
        for w in sentence.split():
            curr = ""
            node = trie
            for c in w:
                node = node[c]
                curr += c
                if '#' in node:
                    break
            words.append(curr)
        return " ".join(words)
        