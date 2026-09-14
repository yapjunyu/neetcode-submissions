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
        # first pass create copies of all the nodes
        hmap = {}
        first = res = head 
        while head:
            hmap[head] = Node(head.val, head.next, head.random)
            head = head.next
        while first:
            copy = hmap[first]
            if copy.next:
                copy.next = hmap[copy.next]
            if copy.random:
                copy.random = hmap[copy.random]
            first = first.next
        return hmap[res] if res else head
        