class MyHashSet:
    def __init__(self):
        # Doing this the 'right' way now, but still seems wicked slow :(
        self.capacity = 15000
        self.hash_set = [[] for _ in range(self.capacity)]

    def get_hash_value(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        hash_value = self.get_hash_value(key)
        if key not in self.hash_set[hash_value]:
            self.hash_set[hash_value].append(key)

    def remove(self, key: int) -> None:
        hash_value = self.get_hash_value(key)
        if key in self.hash_set[hash_value]:
            self.hash_set[hash_value].remove(key)

    def contains(self, key: int) -> bool:
        hash_value = self.get_hash_value(key)
        if key in self.hash_set[hash_value]:
            return True
        return False

    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)