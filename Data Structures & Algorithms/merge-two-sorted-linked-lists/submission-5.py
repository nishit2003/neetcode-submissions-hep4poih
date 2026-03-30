# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode()
        curr = Dummy

        while list1 and list2:
            v1 = list1.val if list1 else 0
            v2 = list2.val if list2 else 0

            if v1 > v2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        
        if list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        if list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        return Dummy.next