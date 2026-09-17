class Node:
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # stores the key and pointer to the node
        self.left, self.right = Node(0, 0), Node(0, 0) # init left and right dummy node
        self.left.next = self.right
        self.right.prev = self.left

    # helper function to remove node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # helper function to insert on the right
    def insert(self, node):
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.next, node.prev = self.right, prev    
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to shift node to the right to update
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        
        
