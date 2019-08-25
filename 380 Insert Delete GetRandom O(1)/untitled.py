from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums) - 1
        self.nums.append(val)
        return True
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        index = self.pos[val]
        self.nums[index] = self.nums[-1]
        self.pos[self.nums[-1]] = index
        self.pos.pop(val)
        self.nums.pop()
        return True
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.nums:
            return self.nums[randint(0, len(self.nums) - 1)]

if __name__ == '__main__':
    sol = RandomizedSet()
    sol.insert(1)
    sol.insert(2)
    sol.insert(3)
    sol.insert(4)
    sol.remove(4)
    sol.remove(2)
    sol.remove(3)
    sol.remove(3)