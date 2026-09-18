"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 2 pass first create all copies of the nodes then map them
        cache = {}
        first = res = head
        while head:
            cache[head] = Node(head.val, head.next, head.random)
            head = head.next
        while first: 
            copy = cache[first]
            if copy.next:
                copy.next = cache[copy.next]
            if copy.random:
                copy.random = cache[copy.random]
            first = first.next
        return cache[res] if res else head

        
        