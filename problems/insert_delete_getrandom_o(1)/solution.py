from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = dict()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # print("insert: ", val)
        if val in self.pos: return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # print("remove: ", val)
        idx = self.pos.get(val, -1)
        if idx < 0: return False
        # print(idx, len(self.nums))
        self.pos[self.nums[-1]] = idx
        self.nums[idx] = self.nums[-1]
        self.nums.pop()
        self.pos.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = randint(0, len(self.nums) - 1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()