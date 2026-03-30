# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        for i in range(1,len(lists)):
            lists[i] = self.merge(lists[i-1],lists[i])
            
        return lists[-1]
    
    def merge(self,l1,l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            if v1 > v2:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        
        if l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        
        if l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
                
        return dummy.next    