from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = set()
        def parse(s):
            name, time, amt, city = s.split(",")
            return (name, int(time), int(amt), city)
        transactions = [parse(s) for s in transactions]
        persons = defaultdict(list)
        for name, time, amt, city in transactions:
            if amt > 1000:
                ans.add("{},{},{},{}".format(name, time, amt, city))
            persons[name].append((time, amt, city))
        for name in persons.keys():
            persons[name].sort()
        for name, ops in persons.items():
            for i, (time1, amt1, city1) in enumerate(ops):
                for j, (time2, amt2, city2) in enumerate(ops):
                    if i != j and abs(time1 - time2) <= 60 and city1 != city2:
                        ans.add("{},{},{},{}".format(name, time1, amt1, city1))
        return list(ans)
                