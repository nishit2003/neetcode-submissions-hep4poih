# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        if not lists: return None
        for i in range(len(lists)-1):
            lists[i+1] = self.merge(lists[i],lists[i+1])
        
        return lists[-1]
        

    def merge(self,l1,l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            v1 = l1.val if l1 else None 
            v2 = l2.val if l2 else None 
            if v1 < v2:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
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