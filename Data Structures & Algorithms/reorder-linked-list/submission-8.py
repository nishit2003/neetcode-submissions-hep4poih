# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1 split in 3 halfs
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next

        #2 reverse the second halve

        second = slow.next
        prev = None
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #3 merge the 2 halves
        first = head
        second = prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2