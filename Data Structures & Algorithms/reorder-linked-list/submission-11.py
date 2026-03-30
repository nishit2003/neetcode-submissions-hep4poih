# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = Node = ListNode()
        # divide
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        # print("second ",second.val)

        # revervse second half
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second=prev
        curr = dummy
        
        # merge and update pointers
        while head or second:
            if head:
                curr.next = head
                head = head.next
                curr = curr.next
                curr.next = None
            if second:
                curr.next = second
                second = second.next
                curr = curr.next
                curr.next = None
            
                
        # return dummy.next

