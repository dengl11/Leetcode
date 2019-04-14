from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = Counter()
        for cp in cpdomains:
            n, domain = cp.split()
            n = int(n)
            c[domain] += n
            parts = domain.split('.')
            for i in range(1, len(parts)):
                c['.'.join(parts[i:])] += n
        return ["{} {}".format(n, s) for (s, n) in c.items()]