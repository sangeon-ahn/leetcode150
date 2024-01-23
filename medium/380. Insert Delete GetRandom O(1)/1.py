import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        
        self.dic[val] = len(self.a)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.arr:
            return False
        
        num = self.arr.pop()
        idx = self.dic.pop(val)

        if idx < len(self.arr):
            self.arr[idx], self.dic[num] = num, idx
        
        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)

        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()