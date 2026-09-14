from typing import Optional

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.head = Node(0, 0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_head(self, node) -> None:
    
        next_node = self.head.next
        self.head.next = node
        node.next = next_node
        node.prev = self.head
        node.next.prev = node 

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_head(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        self._add_head(node)

        if len(self.cache) > self.capacity:
            lru_tail = self.tail.prev
            self._remove(lru_tail)
            
            del self.cache[lru_tail.key]


