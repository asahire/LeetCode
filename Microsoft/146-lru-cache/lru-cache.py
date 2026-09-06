class Node:
    def __init__(self, key:int = 0, value:int = 0):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node()   # head.next = MRU
        self.tail = Node()   # tail.prev = LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def unlink(self, node:Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node 
            
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.unlink(node)
        self.push_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.unlink(self.map[key])

        # add item in cache
        self.node = Node(key, value)
        self.map[key] = self.node
        self.push_front(self.node)
        
        # if cache is full, evict LRU
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self.unlink(lru)
            del self.map[lru.key]   


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)