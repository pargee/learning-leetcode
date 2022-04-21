class MyHashSet:
    def __init__(self):
        self.hash_size = 1000001
        self.hash_set = [None] * self.hash_size

    def contains_hash_value(self, key):
        if key == 0:
            return True
        return key % self.hash_size

    def add(self, key: int) -> None:
        if self.contains_hash_value(key):
            self.hash_set[key] = key

    def remove(self, key: int) -> None:
        if self.contains_hash_value(key):
            self.hash_set[key] = None

    def contains(self, key: int) -> bool:
        if key >= self.hash_size:
            return False
        return self.hash_set[key] is not None

    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)