class LRUNode:

    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.first, self.last = LRUNode(0,0), LRUNode(0,0)
        self.first.next, self.last.prev = self.last, self.first

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #get the key, remove the node, add the node to the end
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = LRUNode(key,value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            LRU = self.first.next
            self.remove(LRU)
            del self.cache[LRU.key]
            

    def add(self, node: int) -> None:
        prev, next = self.last.prev, self.last
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def remove(self, node:int) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        