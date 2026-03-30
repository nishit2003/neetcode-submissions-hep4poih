# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next  # Move slow forward by one
            fast = fast.next.next  # Move fast forward by two

        # Step 2: Reverse the second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp  # Corrected from 'temp' to 'tmp'

        # Step 3: Merge the two halves
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1  # Move first forward
            second = tmp2  # Move second forward
