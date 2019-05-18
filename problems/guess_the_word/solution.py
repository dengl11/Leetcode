# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
from collections import defaultdict
from random import choice
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        nbrs = defaultdict(lambda:defaultdict(list))
        n = len(wordlist)
        def sim(w1, w2):
            return sum(c1 == c2 for(c1, c2) in zip(w1, w2))
        for i in range(n):
            for j in range(i+1, n):
                s = sim(wordlist[i], wordlist[j])
                nbrs[wordlist[i]][s].append(wordlist[j])
                nbrs[wordlist[j]][s].append(wordlist[i])
        candidates = set(wordlist)
        blacklist = [set() for _ in range(6)]
        guesses = 0
        while candidates:
            w = min(candidates, key = lambda w: len(candidates & set(nbrs[w][0])))
            candidates.remove(w)
            if any(w[i] in blacklist[i] for i in range(6)): continue
            s = master.guess(w)
            guesses += 1
            if s == 6 or guesses >= 10: 
                return
            if s == 0:
                for i in range(6):
                    blacklist[i].add(w[i])
            candidates &= set(nbrs[w][s])
