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
        data = {None:None} #original:copy

        curr = head
        while curr:
            copy = Node(curr.val)
            data[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = data[curr]
            copy.next = data[curr.next]
            copy.random = data[curr.random]
            curr = curr.next
        
        return data[head]